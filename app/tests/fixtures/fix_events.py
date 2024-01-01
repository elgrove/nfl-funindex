import pytest


@pytest.fixture
def mock_eventbridge_client():
    """Mocking the boto EventBridge client."""

    class MockEventBridgeClient:
        def __init__(self, *args, **kwargs):
            self.events = []

        def put_events(self, Entries):
            """Mocking boto put_events.

            Args:
                Entries: list
            """
            for entry in Entries:
                self.events.append(entry)

    yield MockEventBridgeClient()


@pytest.fixture
def game_to_scrape_event(client):
    """Yields a CloudWatch aka EventBridge event that a lambda would be invoked with."""
    yield client.events.generate_cw_event(
        "nfl_checker",
        "game_to_scrape",
        {"game_id": "202312160det"},
        [],
    )
