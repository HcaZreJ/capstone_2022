# This v2 is adapted from news_to_vector_v1.py that had 3 main changes:
# 1. It used the  Google Universal Sentence encoder instead of
#    Google News Word2Vec to turn news article text into vector
#    representations and record their similarity.
# 2. Instead of the entire News article content, only the headline
#    of the article is used in the GUSE model to convert to a 
#    vector, to prevent too much news article content from diluting
#    the vector representation.
# 3. The headline is fed into the GUSE model entirely without
#    taking out any stopwords or punctuation, because GUSE is actually
#    case sensitive. Making words lowercase / taking out punctuation /
#    removing stopwords changes the resulting embedding, which might
#    change the outcome of my task. Since the example usages provided
#    by Google did not do any of the above, I presume that I should 
#    retain the original format of the text.

################################## Web-crawling News data ##################################
# 1. Load the pre-trained Google Universal Sentence Encoder model & turn all news article
#    headlines into a vector representation of the article.
# 2. Save the vectors locally as a news_vectors.npy file
# 3. Create a similarity matrix that stores the similarity between every pair of news articles
# 4. Save the similarity matrix locally as a similarity_matrix_v2.npy file

########################### Import all of the necessary packages ###########################
# Built-in modules
import os

# Data manipulation module
import pandas as pd
import numpy as np

# Import tensorflow & tensorflow hub, to utilize the GUSE model
import tensorflow as tf
import tensorflow_hub as hub

##############################     1     ##############################
# Load our news article content data from local csv file
# Note: the folder is specified because the current working directory
# that my IDE uses when I run the script is DEMO_WEB_APP
if os.path.isfile('data_crawling_and_transformation/data_v2.csv'):
    # Read News article data csv
    df = pd.read_csv('data_crawling_and_transformation/data_v2.csv', header=0, index_col=0, 
                     dtype={'source' : str,
                            'author' : str,
                            'title' : str,
                            'description' : str,
                            'url' : str,
                            'urlToImage' : str,
                            'publishedAt' : object,
                            'content' : str},
                     parse_dates=['publishedAt'],
                     infer_datetime_format=True)
# If not found, raise an error
else:
    raise FileNotFoundError("data_v2.csv not created or not in same directory.\nRun news_crawl_v2.py first before you run this script.")

# Load the Google Universal Sentence Encoder model from local memory
embed = hub.load("data_crawling_and_transformation/universal-sentence-encoder_4/")

# Embed the New Article Titles using GUSE
embeddings = embed(df['title'].values)

##############################     2     ##############################
# Turn the embeddings into a numpy array to make it save-able locally
embeddings_array = np.array(embeddings)

# Save the embeddings locally as a .npy file
# It is okay that we overwrite the previous version, because in the 
# news_crawl_v2.py script we already checked for duplicates and discarded them
np.save('data_crawling_and_transformation/embeddings_v2.npy', embeddings_array)

##############################     3     ##############################
# We will be creating a similarity matrix using numpy's inner product
# method. This works just the same as the cosine similarity score
# from ScikitLearn and is much more efficient because it's numpy
similarity_matrix_v2 = np.inner(embeddings_array, embeddings_array)

##############################     4     ##############################
# Save the similarity_matrix_v2 locally as a .npy file
# It is okay that we overwrite the previous version, because in the 
# news_crawl_v2.py script we already checked for duplicates and discarded them
np.save('data_crawling_and_transformation/similarity_matrix_v2.npy', similarity_matrix_v2)