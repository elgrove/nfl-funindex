import pytest
import requests_mock


@pytest.fixture
def mock_requests_schedule_page(fix_schedule_html):
    """Mocks Salesforce token generation and Pardot API responses, both 200."""
    with requests_mock.Mocker() as mock:
        mock.get(
            "https://www.pro-football-reference.com/years/2023/games.htm",
            text=fix_schedule_html,
        )
        yield mock


@pytest.fixture
def mock_requests_game_page(fix_game_html):
    """Mocks Salesforce token generation and Pardot API responses, both 200."""
    with requests_mock.Mocker() as mock:
        mock.get(
            "https://www.pro-football-reference.com/boxscores/202312160det.htm",
            text=fix_game_html,
        )
        yield mock
