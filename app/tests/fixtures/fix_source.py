import pytest

from tests.cases.case_game import GAME_PAGE
from tests.cases.case_schedule import SCHEDULE_PAGE


@pytest.fixture
def fix_schedule_html():
    """Yields a string of the source's schedule page HTML."""
    yield SCHEDULE_PAGE


@pytest.fixture
def fix_game_html():
    """Yields a string of the source's game data page HTML."""
    yield GAME_PAGE
