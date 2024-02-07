# Import necessary module
import pandas as pd

# Function to process Twitter API response JSON and extract relevant data
def process_twitter_response(response_json):
    # Initialize an empty list to store processed tweet data
    data_tweet_list = []

    # Extract organic results from the Twitter API response
    organic_results = response_json.get('organic_results', [])

    # Iterate through each tweet in the organic results
    for tweet in organic_results:
        # Extract snippet text from the tweet
        data_tweet = {
            'snippet': tweet.get('snippet', ''),
        }
        # Append the processed tweet data to the list
        data_tweet_list.append(data_tweet)

        df =pd.DataFrame(data_tweet_list)
        df['snippet'] = df['snippet'].replace(r'[^a-zA-Z0-9\s.,;:!?]', '', regex=True)

    # Create a pandas DataFrame from the processed tweet data
    return df
