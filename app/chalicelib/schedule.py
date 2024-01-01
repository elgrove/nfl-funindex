from datetime import datetime
from functools import cached_property
import os
import re

from bs4 import BeautifulSoup
import requests


class Schedule:
    """Wrapper around the data source's schedule page, which offers information on the
    games in a given season and links to the individual game data pages."""

    def __init__(self, season=None):
        """Initialise with dependencies."""
        self.season = season or self.get_current_season()
        self._game_ids = set()
        self._game_ids_with_data = set()

    @staticmethod
    def get_current_season():
        """Get the current NFL season, a 4-digit int e.g. 2020.

        Returns:
            current_season (int)
        """
        now = datetime.now()
        if now.month >= 7:
            return now.year
        return now.year - 1

    @property
    def game_ids(self):
        """Access to all game IDs in the season.

        Returns:
            set
        """
        if not self._game_ids:
            self._hydrate()
        return self._game_ids

    @property
    def game_ids_with_data(self):
        """Access to the game IDs in the season which have happened and have data.

        Returns:
            set
        """
        if not self._game_ids_with_data:
            self._hydrate()
        return self._game_ids_with_data

    def _hydrate(self):
        """Ensures only one call to the source when the client accesses either of the
        game IDs properties."""
        soup = BeautifulSoup(self._page_html, "lxml")
        tags = soup.find("table", id="games").find_all("a")
        for tag in tags:
            if game_id := self._get_game_id_from_anchor_tag(tag):
                self._game_ids.add(game_id)
                if self._tag_game_has_data(tag):
                    self._game_ids_with_data.add(game_id)

    @cached_property
    def _page_html(self):
        """Access to the HTML of the source page.

        Returns:
            str
        """
        response = requests.get(
            f"{os.environ['SCRAPE_TARGET']}/years/{self.season}/games.htm", timeout=10
        )
        return response.text

    def _get_game_id_from_anchor_tag(self, tag):
        """Get a game ID from a BeautifulSoup Tag, if it exists.

        Args:
            tag: bs4.Tag

        Returns:
            str or None
        """
        try:
            return re.findall(r"\d{9}\D{3}", tag.get("href"))[0]
        except IndexError:
            return None

    def _tag_game_has_data(self, tag):
        """Check if a game Tag has happened and has data.

        Args:
            tag: bs4.Tag

        Returns:
            bool
        """
        if tag.text == "boxscore":
            return True
        return False
