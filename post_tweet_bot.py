import tweepy # type: ignore 
from dotenv import load_dotenv # type: ignore
import os
import time

# Load environment variables
load_dotenv()  # this code load your .env file

# Twitter API credentials
consumer_key = os.getenv("CONSUMER_KEY") 
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


if None in (consumer_key, consumer_secret, access_token, access_token_secret):
    raise ValueError("One or more credentials are missing. Check .env file.")

# Initialize tweepy Client (API v2)
client = tweepy.Client(              
    consumer_key=consumer_key,        # The first consumer_key (left side) is a Python variable name you define in the script.
    consumer_secret=consumer_secret,  # The right side, os.getenv("CONSUMER_KEY"), retrieves the value from the .env file via os.getenv.
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Test authentication
try:
    user = client.get_me().data       # extracts the user details and Without .data, you’d get the full response (including metadata).
    print("Authenticated as:", user.name)
except Exception as e:
    print(f"Authentication error: {e}")

# Post a tweet
tweet_text = f"Loving the #Bitcoin community! 🚀 Posted by my Python bot at {time.ctime()}" # timestamp to make each tweet unique, avoiding duplicate tweet errors (187).
try:
    response = client.create_tweet(text=tweet_text)
    print(f"Posted tweet: {tweet_text} (ID: {response.data['id']})") # response.data is a dictionary with the tweet’s data
    time.sleep(5)  # Avoid rate limits
except Exception as e:
    print(f"Error posting tweet: {e}")

    

##########################################################################

# The os library is not just for moving through files. It’s a Python module for interacting with the operating system, including:
    # File/directory operations (e.g., os.listdir(), os.path).
    # Environment variable management (e.g., os.getenv(), os.environ)
    # System commands (e.g., os.system())

    # os.getenv() is used to read credentials from .env via python-dotenv, not for file navigation.

# tweepy is a Python library for interacting with the Twitter/X API, allowing actions like posting tweets, liking, or following users.
    # It simplifies API requests by handling authentication and HTTP calls.

# tweepy.Client is a class in tweepy for accessing Twitter API v2 endpoints (e.g., create_tweet, get_me).
    
    # get_me() is a method of tweepy.Client that retrieves the authenticated user’s profile information (e.g., username, ID) from the Twitter API v2 endpoint /2/users/me.
        # Function:
            # Returns a Response object containing user data (e.g., name, ID, username)
            # Used to verify the Access Token/Secret are valid and linked to your account
                
                # get_me().data
                    # The Response object from get_me() has a .data attribute, which holds the actual user data as a User object (or dictionary in some cases).

    # create_tweet() is a method of tweepy.Client that posts a tweet to Twitter/X using the API v2 endpoint /2/tweets.
        # Argumen text is required and it has the content (up to 280 characters)
            # Optional arguments (not used in your bot):
                # media_ids: List of media IDs for attaching images/videos.
                # poll_options and poll_duration_minutes: For adding a poll
                # quote_tweet_id: To quote another tweet.
                # in_reply_to_tweet_id: To reply to a tweet.
                # exclude_reply_user_ids: To exclude users from replies.
                # place_id: To add a location.
                # tagged_user_ids: To tag users in the tweet.

# time.ctime() is a function from Python’s time module that returns the current time as a formatted string (e.g., Fri Jul 11 14:30:41 2025).
    # it takes no argument

# response.data['id'] accesses the tweet’s unique ID (e.g., 1234567890123456789) from the dictionary.
    # The ID is a string identifying the tweet, useful for tracking or linking (e.g., https://x.com/username/status/1234567890123456789).