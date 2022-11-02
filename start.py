from src.service.scraper import Scraper
from src.utils import config

if __name__ == "__main__":
    scraper = Scraper(config=config)

    tweets = scraper.get_tweets(
        username="0xabcdef123"
    )

    print()