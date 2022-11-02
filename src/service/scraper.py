import tweepy
from src.service.constants import Fields


proxy = {
    "http": "http://v9WgipjW:DzDNuH4P@45.146.27.188:57833",
    "https": "http://v9WgipjW:DzDNuH4P@45.146.27.188:57833",
}

class Scraper:
    def __init__(self, config: dict):
        self.client = tweepy.Client(
            bearer_token=config["BEARER_TOKEN"],
            consumer_key=config["CONSUMER_KEY"],
            consumer_secret=config["CONSUMER_SECRET_KEY"],
            access_token=config["ACCESS_TOKEN"],
            access_token_secret=config["ACCESS_TOKEN_SECRET"],
        )

    # client.session.proxies.update(proxy)
    def get_user(self, username: str):
        user = self.client.get_user(username="DDCBurkinaFaso", user_fields=Fields.user_fields)
        return user

    def get_tweets(self, username: str, pagination_token: int = None):
        user = self.get_user(username=username)

        tweets = self.client.get_users_tweets(
            expansions=Fields.expansions,
            id=user.data.id,
            max_results=100,
            place_fields=Fields.place_fields,
            tweet_fields=Fields.tweet_fields,
            media_fields=Fields.media_fields,
            pagination_token=pagination_token
        )

        return tweets
