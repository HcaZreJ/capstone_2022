# This file defines two python functions, that generates news recommendations depending on
# the context:
# 1. Showing 6 articles to the User to get an initial capture of their preference, if
#     this was their first-time login.
# 2. Showing 6 article recommendations to non-first-time Users.

# Data handling package import
import numpy as np
import pandas as pd
import random as rd
import scipy.stats as sts

# Load news data into runtime memory
df = pd.read_csv('data_crawling_and_transformation/data_v2.csv', header=0, index_col=0, dtype=str,
                 parse_dates=['publishedAt'], infer_datetime_format=True)
embeddings = np.load("data_crawling_and_transformation/embeddings_v2.npy")
similarity_matrix = np.load("data_crawling_and_transformation/similarity_matrix_v2.npy")

# This is a scale parameter that controls the variance of the normal distribution
# for which new recommendations will be sampled from. Larger means less similar
# recommendations, while smaller means more similar recommendations.
# Since the min and max of our embeddings array is -0.11828855 and 0.11586841,
# let's set this to be 0.025, so that 95% of data only reaches 0.05
sigma = 0.025

def non_first_recommend(user, x=6):
    """
    Function that returns x number of recommendations to non-first-time users.
    Non-first-time recommendation is conducted by sampling a point from the captured
    user preference probability density distribution, and then finding an article in
    our database that is closest to the sampled point.

    Keyword arguments:
    user -- a User object, as defined in models.py
    x    -- the number of recommendations requested, defaults to 6
    """
    # Retrieve all articles that the user has rated
    rated_news = user.news

    # Obtain a list of all scores rated, and a list of news ids
    all_scores = []
    news_ids = []
    for a_rated_news in rated_news:
        all_scores.append(a_rated_news.rating)
        news_ids.append(a_rated_news.news_id)

    # Calculate a sum score & a cumsum score
    sum_score = np.sum(all_scores)
    cumsum_score = np.cumsum(all_scores)

    # Create a holder to place all the news recommended
    recommendations = []

    # Generate x recommendations
    for i in range(x):
        # Obtain 1 random number in between 0 and sum_scores
        article_place = sts.uniform(loc=0, scale=sum_score).rvs()

        # Search the cumulative sum to see which article would we be basing around
        place = np.searchsorted(cumsum_score, article_place)

        # For the article that this recommendation is based around, obtain its 512 dim
        # vector, use these as the mean of Normal distributions, and draw a random
        # sample from each of the Normal d., then look for the closest article & recommend

        # Obtain Article's vector
        article_vec = embeddings[user.news[place].news_id, :]
        # Create an empty sample vector of same dimensions
        sampled_vec = np.zeros(article_vec.shape)

        # For each dimension of the article's vector, we sample a value from a
        # normal distribution built around it
        for i, dim_value in enumerate(article_vec):
            sampled_vec[i] = sts.norm.rvs(loc=dim_value, scale=sigma)

            # Find the index of the article in our database that the user have not seen 
            # before, and is most similar to the sampled article vector
            k = -1
            similarities = np.inner(sampled_vec, embeddings)
            sorted_similarities = np.sort(similarities)
            # Establish an infinite loop to find the an article not seen by the user
            while True:
                next_largest_similarity_score = sorted_similarities[k]
                # This is the index for the next most similar article
                index = np.where(similarities == next_largest_similarity_score)[0][0]
                
                # Compare the next most similar article against every article that the user has seen
                for seen_news in news_ids:
                    # If the user has seen this article before
                    if np.array_equal(embeddings[seen_news], embeddings[index]):
                        # We decrement k by 1, to look for the next most similar, and break out of the for loop
                        k -= 1
                        break
                # This else-clause executes when the for loop completes as normal, meaning
                # the user has not seen this article before, so we break out of the outer infinite while loop
                else:
                    break

            # Add all relevant data of this news article to the list
            recommendations.append(df.iloc[index, :])

    return recommendations


def first_recommend(x=6):
    """
    Function that returns x number of recommendations to first-time users.
    First-time recommendations is done by sampling a random article in the database,
    and then finding the article that is most different from it, in an attempt to
    span the state space as much as possible.

    Keyword arguments:
    x    -- the number of recommendations requested, defaults to 6
    """
    # Holder for the news recommended
    recommendations = []

    # We are going to select a random article, then also select the article that
    # is the exact semantic opposite of this article, to attempt to span the state
    # space as much as possible. We will be repeating this 3 times to show an initial 6 articles.
    for i in range(x):

        # If we are on even number loops (Note: loops start at 0)
        if i % 2 == 0:
            # Draw 1 random sample from the dataset
            index = rd.choice(df.index.values)
            recommendations.append(df.iloc[index, :])

        # Else we are on odd number loops, and we draw sample most different from previous sample
        else:
            # Look for the most different article from this one, add to indexes
            sim_scores = similarity_matrix[index, :]
            least_similar = np.sort(sim_scores)[0]
            index = np.where(sim_scores == least_similar)[0][0]
            recommendations.append(df.iloc[index, :])
        
    return recommendations