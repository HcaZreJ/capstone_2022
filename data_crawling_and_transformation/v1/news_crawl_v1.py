################################## Web-crawling News data ##################################
# 1. Set a few News websites to crawl from, e.g. NewYork Times, BBC, CNN.
# 2. Use Newsapi to crawl all of their news article links in the past 3 years
# 3. Crawl all of the news article's content from these links and store as pandas dataframe
# 4. Format all of the news article content to make them vectorizable by a word2vec model
# 5. Save the news article content locally as a data.csv file

########################### Import all of the necessary packages ###########################
# Built-in modules
import requests
import time
import sys
import os

# String formatting modules
from contractions import fix
from string import punctuation
from nltk.corpus import stopwords

# Data manipulation module
import pandas as pd

# BeautifulSoup is a package frequently used in Python for html formatting
from bs4 import BeautifulSoup

##############################     1     ##############################
# Set the sources that we are going to crawl from
# Since this is a draft we won't worry about #sourcequality yet.
# The sources are decided from this list: https://www.top10.com/news-websites
# There isn't New York Times & NPR in Newsapi, so it won't be included either for now
# Google News is a search engine that shows news from other news websites, which makes crawling
# too hard, so won't be included either
sources = 'cnn,reuters,the-wall-street-journal,bbc-news,fox-news,nbc-news,the-washington-post'
# Note: To see all of the sources offered by Newsapi, visit: https://newsapi.org/v2/sources?apiKey=e938341216df4163be5f15cb92d413e6

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
# floor division by 100 + 1 times in total
totalCrawlsNeeded = totalResults//100 + 1

# However, due to using an upaid plan, I am actually only allowed 100 requests
# per day. Thus this will be instead set to 100
totalCrawlsNeeded = 100

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
        # Variable to hold the list of article information
        articles = output['articles']
    except KeyError:
        break

    # Create dataframe from the list of dictionaries, if not present, else just concatenate
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
# This is problematic and will be decreased in future iterations of the
# product.
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
    if successful:
        df.iloc[index, -1] = content
    # If failed then we gather the failure's info
    else:
        failure_info.append(content)

    # Sleep for 2 seconds to avoid overloading
    time.sleep(2)

##############################     4     ##############################
# First we need to do some formatting. Right now the 'content' column
# of our df is really messy. Let's define a function to do that
def format_string(text):
    '''
    Formats a string of text to make it more standardized. Includes
    the following operations in the exact order:
    1. Removes contractions, e.g. I'll -> I will
    2. Removes punctuations, e.g. That is it. -> That is it
    3. Removes numbers, e.g. 300 turtles -> turtles
    4. Removes extra space, e.g. you  are right -> you are right
    5. Makes words lowercase, e.g. Terminal -> terminal
    6. Removes stop words (i.e. words that don't add value to our analysis),
        e.g. the library -> library
    '''
    # 1. Removes contractions
    # This fix() function is imported at the top from the contractions module
    text = fix(text)

    # 2. Removes punctuation
    # This punctuation string is imported at the top from the string module
    translator = str.maketrans(punctuation, ' '*len(punctuation)) # map punctuation to space
    text = text.translate(translator)

    # 3. Removes numbers
    text = ''.join([i for i in text if not i.isdigit()])

    # 4. Removes extra space
    text = ' '.join(text.split())

    # 5. Makes lowercase
    text = text.lower()

    # 6. Removes stop words
    # This stopwords is imported at the top from the nltk.corpus module
    stop = stopwords.words('english')
    text = " ".join([word for word in text.split() if word not in (stop)])

    # Return the result
    return text

# Next we are going to format all of the news article content
# Define a list to hold all of the formatted strings
formatted_contents = []
for index, row in df.iterrows():
    # Format the text
    formatted_string = format_string(row['content'])

    # Add the formatted text to list
    formatted_contents.append(formatted_string)

# Insert this list as a new column into our df
df['Formatted content'] = formatted_contents

# If formatted content is empty, then something went wrong in the previous
# process (likely with web crawling). To avoid it interrupting subsequent
# code, we are going to delete the row from the df
delete_indexes = []
for index, row in df.iterrows():
    if not row['Formatted content']:
        delete_indexes.append(index)

df = df.drop(index = delete_indexes)
# Reset indexes
df = df.reset_index(drop = True)

##############################     5     ##############################
# Save news article data, if there isn't one already
if not os.path.isfile('data.csv'):
    df.to_csv('data.csv')
# Else need to write data on top of already crawled data,
# by reading past data, taking out duplicates, and saving again
else:
    # Read already crawled data into working memory
    current_data = pd.read_csv('data.csv', header=0, index_col=0, 
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
    # Obtain the url of news articles that currently exist
    existing_urls = current_data['url'].values
    # For each row in our newly crawled data
    for index, row in df.iterrows():
        # If the row's url does not exist in previously crawled urls
        if row['url'] not in existing_urls:
            # Add the row to the current_data dataframe
            current_data = current_data.append(row, ignore_index=True)

    # Finally, save to new csv
    current_data.to_csv('data.csv')
