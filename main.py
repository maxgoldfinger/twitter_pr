import requests
from environment import config
import tweepy
from constants import Fields


proxy = {
    "http": "http://v9WgipjW:DzDNuH4P@45.146.27.188:57833",
    "https": "http://v9WgipjW:DzDNuH4P@45.146.27.188:57833",
}

client = tweepy.Client(
    bearer_token=config.BEARER_TOKEN,
    consumer_key=config.CONSUMER_KEY,
    consumer_secret=config.CONSUMER_SECRET_KEY,
    access_token=config.ACCESS_TOKEN,
    access_token_secret=config.ACCESS_TOKEN_SECRET,
)

# client.session.proxies.update(proxy)

user_fields = ["protected"]
try:
    user = client.get_user(username="elonmusk", user_fields=user_fields)
except requests.exceptions.SSLError:
    print(1)

token = None
c = 0
tweet_count = 0
while True:
    print(f"Page {c+1}")
    c += 1
    try:
        tweets = client.get_users_tweets(
            expansions=Fields.expansions,
            id=user.data.id,
            max_results=100,
            place_fields=Fields.place_fields,
            tweet_fields=Fields.tweet_fields,
            media_fields=Fields.media_fields,
            pagination_token=token
        )
    except requests.exceptions.SSLError:
        print(1)
        break
    print()
    tweet_count += len(tweets.data)
    token = tweets.meta.get("next_token", "")
    if not token:
        break

print()
