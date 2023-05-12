# Web-crawling code (Version 2)

This folder contains all the scripts for web-crawling news article data and converting them to 512-dimensional vector embeddings using the Google Universal Sentence Encoder (GUSE).

Scripts are run in the order of:

1. <code>news_crawl_v2.py</code>, which updates the <code>data_v2.csv</code> file, adding newly crawled news articles to the csv, and deleting entries too old.

2. <code>news_to_vector_v2.py</code>, which updates the <code>embeddings_v2.npy</code> and the <code>similarity_matrix_v2.npy</code> file, to contain all newly transformed embeddings of the crawled articles from <code>data_v2.csv</code>.

The `universal-sentence-encoder_4` folder contains the GUSE model that gets loaded in `news_to_vector_v2.py`.

The `test.ipynb` file is a Jupyter notebook that I use to run tests on the data collected. It currently contains some <b>Exploratory Data Analysis</b> on the variance of the transformed vectors in the dataset.