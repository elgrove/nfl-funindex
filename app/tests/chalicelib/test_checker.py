from unittest.mock import patch, PropertyMock

import pytest

from chalicelib.checker import Checker
from chalicelib.schedule import Schedule
from chalicelib.table import DataTable


class MockPublisher:
    """Mocking the abstract base Publisher."""

    def __init__(self):
        """Init."""
        self.published = []

    def publish(self, items):
        """Mocks Publisher.publish interface."""
        for item in items:
            self.published.append(item)


@pytest.mark.unit
class TestChecker:
    @patch("chalicelib.schedule.Schedule.game_ids_with_data", new_callable=PropertyMock)
    def test_check(
        self,
        mock_game_ids_with_data,
        data_table,
    ):
        """Given an empty database and a schedule with 2 games with data

        When the Checker.check method is called

        Then the Publisher receives 2 events
        """
        table = DataTable(table=data_table)
        mock_publisher = MockPublisher()
        mock_game_ids_with_data.return_value = ["20200101abc", "20200102def"]
        checker = Checker(table, Schedule(), mock_publisher)
        checker.check()
        assert len(mock_publisher.published) == 2
        assert all(
            id in mock_publisher.published for id in ["20200101abc", "20200102def"]
        )
