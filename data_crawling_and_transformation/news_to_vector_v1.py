################################## Web-crawling News data ##################################
# 1. Load the pre-trained Google-News Word2Vec model & turn all news article content into
#       an average of all of the vector of its words
# 2. Create a similarity matrix that stores the similarity between every pair of news articles
# 3. Save the similarity matrix locally as a similarity_matrix.npy file

########################### Import all of the necessary packages ###########################
# Built-in modules
import os

# Data manipulation module
import pandas as pd
import numpy as np

# Gensim is a ML library frequently used in Python for NLP purposes
import gensim

# Import cosince similarity from sklearn to compute similarity scores
from sklearn.metrics.pairwise import cosine_similarity

##############################     1     ##############################
# Load our news article content data from local csv file
if os.path.isfile('data.csv'):
    # Read News article data csv
    df = pd.read_csv('data.csv', header=0, index_col=0, 
                     dtype={'source' : str,
                            'author' : str,
                            'title' : str,
                            'description' : str,
                            'url' : str,
                            'urlToImage' : str,
                            'publishedAt' : object,
                            'content' : str,
                            'Formatted content' : str},
                     parse_dates=['publishedAt'],
                     infer_datetime_format=True)
# Else raise an error to tell user that data is not crawled yet
else:
    raise FileNotFoundError("data.csv not created or not in same directory.\nRun news_crawl_v1.py first before you run this script.")

# Load the pre-tained google-news word2vec model
model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

# Define a function, that takes the model & a string of text as input
# and outputs the averaged vector over the text.
def text_to_average_vector(model, text):
    '''
    Using a gensim model, converts each word in the text string into
    a vector, averages over all these vectors, and returns the average.

    The simple average is used in the first try, in future TF-IDF will
    be used to better capture the importance of a word in a piece of text.
    '''
    # Split the text into a list of words
    words = text.split()

    # Create an empty numpy array, with ncol = number of words, and
    # nrow = output dimensions of the model
    all_vectors = np.zeros((model.vector_size, len(words)))

    # If our model is large, then it would be reasonable for us to assume that 
    # any word that cannot be found in the model is not a word, e.g. â or ©
    # If such words are encountered, it also means that we need to delete a
    # column from our vector of all the words, to avoid disrupting the subsequent
    # average, thus define a list to hold the column indexes that we are going to
    # delete later:
    col_to_delete = []

    # Looping over all words, turn them into vectors and insert into np array
    for i in range(len(words)):
        try:
            vector = model.get_vector(words[i])
        # If the word cannot be found in the model, we will need to delete this
        # column from our array of vectors
        except KeyError:
            col_to_delete.append(i)
            continue

        # Insert this vector at the right position
        # a[:, 0] means select all rows from column 0
        all_vectors[:, i] = vector

    # Delete the columns in which the word cannot be found in the model
    final_vec = np.delete(all_vectors, col_to_delete, axis = 1)

    # Average over the columns, and return the averaged vector
    averaged_vec = np.mean(final_vec, axis = 1)
    return averaged_vec

# For all of our news articles, obtain an averaged vector of its news content,
# and add as a new column to our df
df_vectors = []
for index, row in df.iterrows():
    news_vector = text_to_average_vector(model, row['Formatted content'])
    df_vectors.append(news_vector)

##############################     2     ##############################
# I've tried the n_similarity function given by the model, but it did
# not work so well. I think it is because of the enormous amount of words
# that made the model think every pair of articles is similar. The minimum
# of all of them is 0.97 (which does not make enough sense), and it takes
# a long time to run as well. Thus instead I created an average vector on my
# own, and computed their cosine similarity. It is still not very good, but
# it's better than all news articles being similar (good enough for a 1st draft).

# This functions scales with θ(n^2), which makes it take a lot of time when
# there are a lot of news articles. It will be improved in the next iteration.
def make_similarity_matrix(iterable):
    '''
    Creates a similarity matrix given an iterable of vectors that each
    represents the semantic position of a news article.
    Requires an iterable of vectors as input.
    '''
    # Create an empty matrix
    similarity_matrix = np.zeros((len(iterable), len(iterable)))

    # Looping over all the entries in the iterable
    for i in range(len(iterable)):
        # Compare row's vector against every other row's vector
        for j in range(len(iterable)):
            # Reshape the vectors for use in sklearn's function
            vec1 = iterable[i].reshape(1, -1)
            vec2 = iterable[j].reshape(1, -1)

            # Compute score using cosine similarity
            score = cosine_similarity(vec1, vec2)

            # Add the score to our matrix
            similarity_matrix[i, j] = score

    return similarity_matrix

# Make a similarity matrix for all the news articles that we've recorded
similarity_matrix = make_similarity_matrix(df_vectors)

##############################     3     ##############################
# Save similarity_matrix with numpy, if there isn't one already
if not os.path.isfile('similarity_matrix.npy'):
    np.save('similarity_matrix.npy', similarity_matrix)