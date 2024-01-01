from abc import ABC, abstractmethod
from itertools import islice
import json

import boto3


class Publisher(ABC):
    """Abstract base of a message publisher to publish game IDs to be scraped by a
    downstream service.

    This publisher must offer a .publish() interface but could use any message queue or
    event service (that the scraper is capable of listening to)
    """

    @abstractmethod
    def publish(self, items):
        """Publish the items."""


class EventPublisher(Publisher):
    """Publishes game IDs to be scraper to the AWS EventBridge event bus."""

    def __init__(self, client=None):
        """Initialise with dependencies."""
        self.client = client or boto3.client("events")

    def _batched_items(self, items, batch_size=10):
        """Batch a list of items into nested lists of given length.

        So with batch size 2 this [1,2,3,4,5,6]
        becomes this [[1,2],[3,4],[5,6]]

        Args:
            items: iterable
            batch_size: int

        Returns:
            list[list]
        """
        iterator_ = iter(items)
        return iter(lambda: list(islice(iterator_, batch_size)), [])

    def publish(self, items):
        """Publish the game IDs that require scraping to EventBridge, in batches of 10.

        Args:
            items: iterable[dict]
        """
        for batch in self._batched_items(items):
            entries = [
                {
                    "Source": "nfl_checker",
                    "Detail": json.dumps({"id": item}),
                    "DetailType": "game_to_scrape",
                }
                for item in batch
            ]
            self.client.put_events(Entries=entries)
