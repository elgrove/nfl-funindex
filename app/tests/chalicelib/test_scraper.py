from unittest.mock import patch, PropertyMock

import pytest

from chalicelib.scraper import GameScraper, GameScraperDirector
from chalicelib.table import DataTable


@pytest.mark.unit
class TestGameScraperDirector:
    @patch("chalicelib.scraper.GameScraper.game_data", new_callable=PropertyMock)
    def test_director_scrape(self, mock_game_data, single_game_data, data_table):
        """Given an empty data table and a dict of scraped data

        When the scrape method is called

        Then the game data is stored in the table
        """
        table = DataTable()
        table._table = data_table
        scraper = GameScraper("20200101abc")
        mock_game_data.return_value = single_game_data
        director = GameScraperDirector(table, scraper)
        director.scrape()
        scan = data_table.scan()
        assert scan["Items"][0] == single_game_data


@pytest.mark.unit
class TestScraper:
    GAME_ID = "202312160det"

    def test_game_data(self, mock_requests_game_page, single_game_data):
        """Given a page of game data, test that the scraper returns data including the computed fun index."""
        scraper = GameScraper(self.GAME_ID)
        data = scraper.game_data
        assert isinstance(data, dict)
        assert data == single_game_data
