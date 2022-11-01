import os
from dataclasses import dataclass, asdict


# @dataclass
# class config:
#     CONSUMER_KEY: str = os.environ["CONSUMER_KEY"]
#     CONSUMER_SECRET_KEY: str = os.environ["CONSUMER_SECRET_KEY"]
#     BEARER_TOKEN: str = os.environ["BEARER_TOKEN"]
#     ACCESS_TOKEN: str = os.environ["ACCESS_TOKEN"]
#     ACCESS_TOKEN_SECRET: str = os.environ["ACCESS_TOKEN_SECRET"]
#
#     def to_dict(self):
#         return asdict(self)


def fetch_tweets(pagination_token: str):
    raw_data = {
        "tweets": ["tweet1", "tweet2", "tweet3"],
        "meta": {
            "token": "7124537612"
        }
    }
    tweets = raw_data['tweets']
    token = raw_data['meta']['token']
    yield token

    yield from tweets


gen = fetch_tweets(pagination_token="12312312312312")
next_token = next(gen)
print(next_token)
tweets = [elem for elem in gen]
print(tweets)
