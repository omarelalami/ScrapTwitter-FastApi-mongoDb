# Import necessary modules
import requests
from scrap.config import api_key, hashtag, num_tweets

# Function to make a request to the Twitter API using Scraper API
def make_twitter_request():
    # Prepare payload with API key, hashtag query, and number of tweets
    payload = {
        'api_key': api_key,
        'query': f'#{hashtag}',
        'num': str(num_tweets)
    }

    # Make a GET request to the Scraper API with the prepared payload
    return requests.get('https://api.scraperapi.com/structured/twitter/search', params=payload)
