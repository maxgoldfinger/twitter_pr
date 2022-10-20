import environment
from environment import config
import tweepy
from constants import Fields
import os

def parse_tweets(config: environment.config):

    client = tweepy.Client(
        bearer_token=config.BEARER_TOKEN,
        consumer_key=config.CONSUMER_KEY,
        consumer_secret=config.CONSUMER_SECRET_KEY,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_TOKEN_SECRET,
    )

    username = "0xABCDEF123"

    user = client.get_user(username=username)

    user_id = user.data.id

    tweets = client.get_users_tweets(
        id=user_id,
        expansions=Fields.expansions,
        max_results=10,
        place_fields=Fields.place_fields,
        tweet_fields=Fields.tweet_fields,
        media_fields=Fields.media_fields,
    )

    tweets_data = tweets.data
    tweets_includes = tweets.includes
    print()


if __name__ == "__main__":
    config_ = config()
    parse_tweets(config=config_)
    print(1)