# This v2 is adapted from news_crawl_v1.py that had 2 main change:
# 1. No longer formats the crawled news article content into a
#    nlp-ready format, i.e. no longer removes stopwords, punctuation,
#    numbers, extra space, or makes words lowercase, and fix contractions.
#    This is because GUSE is case-sensitive. Doing all of the above
#    pre-processing actually changes the meaning of the sentence and
#    causes the GUSE to output a different vector representation.
#    Since the example usages provided by Google did not do any of the
#    above, I presume that I should retain the original format of the text.
# 2. Instead of transforming the news article to vector using the
#    entire article's content, instead this version will be using
#    only the headline of the article to get a vector representation
#    of the article, because as stated in change 1, more words
#    dilutes the meaning and hinders and hinders the performance
#    of the transformer. A summary of the article should make it
#    perform better.
# v1 is not deleted to keep track of progress, and so that I can
# revert back to an older version if things went wrong.

################################## Web-crawling News data v2 ##################################
# 1. Set a few News websites to crawl from, e.g. NewYork Times, BBC, CNN.
# 2. Use Newsapi to crawl all of their news article links in the past 3 years
# 3. Crawl all of the news article's content from these links and store as pandas dataframe
# 4. Save the news article content locally as data_v2.csv file

########################### Import all of the necessary packages ###########################
# Built-in modules
import requests
import time
import sys
import os

# Data manipulation module
import pandas as pd

# BeautifulSoup is a package frequently used in Python for html formatting
from bs4 import BeautifulSoup

##############################     1     ##############################
# Define news crawl sources
sources = 'cnn,reuters,the-wall-street-journal,bbc-news,fox-news,nbc-news,the-washington-post'

# Use a dictionary of dictionaries to set the tags & attributes for which news
# content is stored in each of the above news sources, will be used later in crawling
contentLocation = {
    'cnn': {
        'tag': 'p',
        'class': 'paragraph inline-placeholder'
    },
    'reuters': {
        'tag': 'p',
        'class': 'text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI'
    },
    'the-wall-street-journal': {
        'tag': 'p',
        'class': 'css-xbvutc-Paragraph e3t0jlg0'
    },
    'bbc-news': {
        'tag': 'p',
        'class': 'ssrcss-1q0x1qg-Paragraph eq5iqo00'
    },
    'fox-news': {
        'tag': 'p' # Fox news' article content has no attribute but just a tag <p>
    },
    'nbc-news': {
        'tag': 'p',
        'class': '' # Content is stored under the class attribute with no value on NBC news
    },
    'the-washington-post': {
        'tag': 'p',
        'class': 'wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css font-copy'
    }
}

##############################     2     ##############################
# Set Newsapi.org apiKey that we will be using
apiKey = 'e938341216df4163be5f15cb92d413e6'

# use headers to hide our API key
headers = {'Authorization': 'e938341216df4163be5f15cb92d413e6'}

# Set the API endpoint to crawl data from
everything = "https://newsapi.org/v2/everything?"
top_headlines = "https://newsapi.org/v2/top-headlines?"

# Define keyword for how sources will be sorted
sorby = "popularity"

# Store keywords into a dictionary for use in crawling
params = {'apiKey': apiKey,
          'sources': sources,
          'sortBy': sorby,
          'language': 'en',
          'page': 1}

# Set html requests and get a response object, this is first run to establish
# the total number of articles that we need to crawl
response = requests.get(url = everything, headers = headers, params = params)

# Turn response into a json object, and get the 'totalResults' field
output = response.json()
totalResults = output['totalResults']
# Since each crawl gives a maximum of 100 articles, we would need to crawl
# (floor division by 100) + 1 times in total
totalCrawlsNeeded = (totalResults//100) + 1

# Crawl all of the article urls and store them into our dataframe
for i in range(1, totalCrawlsNeeded+1):
    # Set the page number crawled in this run
    params['page'] = i

    # Send html requests and get response
    response = requests.get(url = everything, headers = headers, params = params)

    # Turn response into a json object
    output = response.json()

    ## Turn the json result into a pandas.dataframe object

    # Our unpaid version limits the number of urls we can get, thus we need to wrap
    # the next line in a try, except block
    try:
        # The 'articles' field is where the actual crawled news articles are stored
        articles = output['articles']
    # This is for when we reached the limit that we can crawl
    except KeyError:
        break

    # Create dataframe from the list of dictionaries, if not present then just concatenate
    try:
        df
        temp = pd.DataFrame(articles)
        df = pd.concat([df, temp], ignore_index = True)
    except NameError:
        df = pd.DataFrame(articles)        

    # Sleep for 2 seconds to avoid overloading the API
    time.sleep(2)

##############################     3     ##############################
# Note: This code cell takes about 33 minuts to run, since it sends 
# about 500 html requests, takes about 2 seconds for every request, and
#  waits for 2 seconds after every request -> 500 * 4 / 60 ≈ 33 minutes

# We are not going to import the function but rather copy&paste it here
# because importing causes python to run news_crawl_v1.py altogether
# once to establish the runtime cache, and that takes too long
def get_news_content(url, tag, class_=None):
    '''
    Crawls a new's content, given the url, tag, and class.

    Returns True & news_content if crawling was successful, else
    returns False, [url, error_type, error_info] if error was encountered.
    '''
    # Since our code might produce errors in the process for various
    # reasons, calling it in a try-except block will make the code run better
    try:
        # Send requests to the url & obtain response object
        response = requests.get(url)

        # Use BeautifulSoup to parse the html response & finding data
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the news content using the given tag & attribute
        if class_:
            content = soup.find_all(tag, class_ = class_)
        else:
            content = soup.find_all(tag)

        # Content is a list of all the html elements found, we need to 
        # further concatenate them together into a string and strip it
        news_content = ''
        for tag_found in content:
            news_content += tag_found.text + ' '

        # Return True & content
        return True, news_content

    # this describes what to do if an exception is thrown 
    except Exception:
        
        # get the exception information
        error_type, error_obj, error_info = sys.exc_info()
        
        # Return False & error info
        return False, [url, error_type, error_obj, error_info]

# Create a list to hold all of the failure info
failure_info = []

# Crawl news article data from all of the urls in the df
for index, row in df.iterrows():
    # Get the url
    url = row['url']

    # Get the id of the news website, then obtain tag & class info
    # using our predefined dictionary
    id = row['source']['id']
    tag = contentLocation[id]['tag']
    # Fox news is the only news website where its article content
    # doesn't have any html attribute but just a tag <p>
    if contentLocation[id] != 'fox-news':
        class_ = contentLocation[id]['class']

    # Crawl news content given the inputs
    if class_:
        successful, content = get_news_content(url, tag, class_)
    else:
        successful, content = get_news_content(url, tag)

    # If successful, then replace the 'content' section of our df with the content
    # Which is the last column, thus can be accessed by df.iloc[index, -1]
    # Note: The 'content' column is provided by Newsapi, but it is limited to ~100 characters
    if successful:
        df.iloc[index, -1] = content
    # If failed then we gather the failure's info
    else:
        failure_info.append(content)

    # Sleep for 2 seconds to avoid website overloading
    time.sleep(2)

##############################     4     ##############################
# Save news article data, if there isn't one already
# Note: the folder is specified because the current working directory
# that my IDE uses when I run the script is DEMO_WEB_APP
if not os.path.isfile('data_crawling_and_transformation/data_v2.csv'):
    df.to_csv('data_crawling_and_transformation/data_v2.csv')
# Else need to write data on top of already crawled data,
# by reading past data, taking out duplicates, and saving again
else:
    # Read already crawled data into working memory
    current_data = pd.read_csv('data_crawling_and_transformation/data_v2.csv', header=0, index_col=0, 
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
    # Obtain the url of news articles that currently exist
    existing_urls = current_data['url'].values
    # For each row in our newly crawled data
    for index, row in df.iterrows():
        # If the row's url does not exist in previously crawled urls
        if row['url'] not in existing_urls:
            # Add the row to the current_data dataframe
            current_data = pd.concat([current_data, row], ignore_index=True)

    # Finally, save to new csv
    current_data.to_csv('data_crawling_and_transformation/data_v2.csv')