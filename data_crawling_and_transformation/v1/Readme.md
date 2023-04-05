# Web-crawling code (Version 1)

This folder contains the old code that did the web-crawling & the transformation of crawled news to 300-dimensional vectors using the Google News Word2Vec model.

Note: This version has been depracated due to Word2Vec not working well on representing news articles. It transforms words to an embedding, whereas news articles are made out of headlines, paragraphs, etc.

Note: The original Google News Word2Vec model is not here in the folder due to size limits (even with git large file storage), so if you are curious / interested in Google News Word2Vec, you can find its documentation [here](https://code.google.com/archive/p/word2vec/) and the model file [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g).