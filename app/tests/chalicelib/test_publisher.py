import pytest

from chalicelib.publisher import EventPublisher


@pytest.mark.unit
class TestEventPublisher:
    def test_publish(self, mock_eventbridge_client):
        """Given items, When the publisher.publish method is called.

        Then the event bus receives the items"""
        publisher = EventPublisher(mock_eventbridge_client)
        items = [{"item": "item1"}, {"item": "item2"}]
        publisher.publish(items)
        assert len(mock_eventbridge_client.events) == 2
        event = mock_eventbridge_client.events[0]
        assert event["DetailType"] == "game_to_scrape"
        assert event["Source"] == "nfl_checker"
