import pytest
from freezegun import freeze_time

from chalicelib.schedule import Schedule


@pytest.mark.unit
class TestGetCurrentSeason:
    @freeze_time("2000-09-01")
    def test_after_july(self):
        """Test the season after July is the current year number."""
        result = Schedule.get_current_season()
        assert result == 2000

    @freeze_time("2000-03-01")
    def test_before_july(self):
        """Test the season before July is the previous year number."""
        result = Schedule.get_current_season()
        assert result == 1999


@pytest.mark.unit
class TestSchedule:
    def test_game_ids(self, mock_requests_schedule_page):
        """Given a schedule page response, test that it contains 272 game IDs."""
        schedule = Schedule()
        assert len(schedule.game_ids) == 272

    def test_game_ids_with_data(self, mock_requests_schedule_page):
        """Given a schedule page response, test that it contains 225 game IDs with data."""
        schedule = Schedule()
        assert len(schedule.game_ids_with_data) == 225
