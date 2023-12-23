from functools import cached_property

from chalicelib import LOGGER


class Checker:
    """Checks source for new games to scrape."""

    def __init__(self, table, schedule, publisher):
        """Initialise with dependencies.

        Args:
            table (DataTable): persistence store
            schedule (Schedule): data source
            publisher(Publisher): event or message publisher
        """
        self._table = table
        self._schedule = schedule
        self._publisher = publisher

    @cached_property
    def game_ids_to_scrape(self):
        """Uses set logic to find the difference between games at source and games in
        data store.

        Returns:
            set
        """
        games_in_table = set(
            self._table.get_game_ids_by_season(self._schedule.get_current_season())
        )
        games_at_source = set(self._schedule.game_ids_with_data)
        return games_at_source - games_in_table

    def check(self):
        """Check source for new games to scrape and send them to the publisher."""
        LOGGER.info(
            "Checked source - %s new games to scrape.", len(self.game_ids_to_scrape)
        )
        self._publisher.publish(self.game_ids_to_scrape)
