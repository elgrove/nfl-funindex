from functools import cached_property
import os

import boto3
from boto3.dynamodb.conditions import Attr, Key


class DataTable:
    """Wrapper around the DynamoDB table holding the app's data."""

    def __init__(self, table=None):
        """Initialise with dependencies."""
        self.name = os.environ["DATA_TABLE"]
        self._resource = boto3.resource("dynamodb")
        self._table = table or self._resource.Table(self.name)

    @property
    def current_season_week(self):
        """Return the most recent season_week, if data exists in the table.

        Returns:
            str
        """
        if data := self._season_weeks:
            return data[-1]
        else:
            return None

    @property
    def previous_season_week(self):
        """Return the second most recent season_week, if data is present in the table.

        Returns:
            str
        """
        try:
            return self._season_weeks[-2]
        except IndexError:
            return None

    @property
    def current_week_games(self):
        """Return a list of dicts each representing a game in the
        self.current_season_week, sorted by fun_index desc.

        Returns:
            list[dict]
        """
        if current := self.current_season_week:
            items = self._query_table_by_season_week(current)
            return self._sort_items_by_fun_index_desc(items)
        else:
            return None

    @property
    def previous_week_games(self):
        """Return a list of dicts each representing a game in the
        self.previous_season_week, sorted by fun_index desc.

        Returns:
            list[dict]
        """

        if previous := self.previous_season_week:
            items = self._query_table_by_season_week(previous)
            return self._sort_items_by_fun_index_desc(items)
        else:
            return None

    def get_game_ids_by_season_week(self, season_week):
        """Returns a list of the game IDs in a given season_week.

        Args:
            season_week: str

        Returns:
            list
        """
        items = self._query_table_by_season_week(season_week)
        return [item["id"] for item in items]

    def get_game_ids_by_season(self, season):
        """Returns a list of the game IDs in a given season.

        Args:
            season: int

        Returns:
            list
        """
        items = self._query_table_by_season(season)
        return [item["id"] for item in items]

    def write_game_data(self, game_data):
        """Writes given game data dict into the table.

        Args:
            game_data: dict
        """
        self._table.put_item(Item=game_data)

    def _query_table_by_season_week(self, season_week):
        """Query the table for items with the matching season_week.

        Args:
            season_week: str

        Returns:
            list[dict]
        """
        response = self._table.query(
            KeyConditionExpression=Key("season_week").eq(season_week),
        )
        return response["Items"]

    def _query_table_by_season(self, season):
        """Query the table for items with the matching season.

        Args:
            season: int

        Returns:
            list[dict]
        """

        response = self._table.scan(
            FilterExpression=Attr("season_week").begins_with(str(season))
        )
        return response["Items"]

    def _sort_items_by_fun_index_desc(self, items):
        """Return a list of dicts sorted by their key fun_index, descending.

        Args:
            items: list

        Returns:
            list
        """
        items = items.copy()
        return sorted(
            items,
            key=lambda d: float(d["fun_index"]),
            reverse=True,
        )

    @cached_property
    def _season_weeks(self):
        """Returns a list of unique season_week values (e.g. '2021-01'), sorted
        ascending.

        Returns:
            list[str]
        """
        response = self._table.scan(
            ProjectionExpression="season_week",
        )
        return sorted({item["season_week"] for item in response["Items"]})
