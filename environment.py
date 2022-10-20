import os
from dataclasses import dataclass, asdict

@dataclass
class config:
    CONSUMER_KEY: str = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET_KEY: str = os.environ["CONSUMER_SECRET_KEY"]
    BEARER_TOKEN: str = os.environ["BEARER_TOKEN"]
    ACCESS_TOKEN: str = os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET: str = os.environ["ACCESS_TOKEN_SECRET"]

    def to_dict(self):
        return asdict(self)
