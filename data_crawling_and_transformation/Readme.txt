This folder contains all of the scripts for web-crawling news article data
and converting them to vector embeddings using the Google Universal Sentence
Encoder.

Scripts are run in the order of:

1. news_crawl_v2.py, which updates the data_v2.csv file, adding newly crawled
    news articles to the csv, and deleting entries too old.
2. news_to_vector_v2.py, which updates the embeddings_v2.npy and the 
    similarity_matrix_v2.npy file, to contain all newly transformed embeddings
    of the crawled articles from data_v2.csv.

The older version of web-crawling is kept in folder v1, too keep track of progress.
It used the Google News Word2Vec instead of GUSE to transform article data to vector
embeddings.