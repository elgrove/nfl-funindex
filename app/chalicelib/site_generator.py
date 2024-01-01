import os

import boto3
from jinja2.environment import Environment as JinjaEnvironment

from chalicelib import LOGGER
from chalicelib.template import PAGE_TEMPLATE


def _round_and_pad_filter(value):
    """Templating filter to round a float to 2 decimal places, padding the second if
    needed.

    e.g. "2.1" becomes "2.10"

    Args:
        value: int or float or numeric string

    Returns:
        str
    """
    try:
        float_value = float(value)
        return f"{float_value:.2f}"
    except ValueError:
        return value


class HtmlRenderer:
    """Renders HTML strings using the Jinja templating engine."""

    def __init__(self, table):
        """Initialise with dependencies.

        Args:
            table (DataTable): persistence store
        """
        self._table = table

    @property
    def _template(self):
        """Access to the Jinja Template Environment.

        Returns:
            jinja2.Environment
        """
        env = JinjaEnvironment(autoescape=True)
        env.filters["round_and_pad"] = _round_and_pad_filter
        return env.from_string(str(PAGE_TEMPLATE))

    def render_current_week(self):
        """Return web page html string for the current week's game.

        Returns:
            str
        """
        games = self._table.current_week_games
        return self._template.render(games=games)

    def render_previous_week(self):
        """Return web page html string for the previous week's games, if they exist.

        Returns:
            str
        """
        if games := self._table.previous_week_games:
            return self._template.render(games=games)
        else:
            return None


class S3Bucket:
    """Wrapper around the S3 bucket for the static website files."""

    NAME = os.environ["SITE_BUCKET_NAME"]

    def __init__(self, resource=None):
        """Initialise with dependencies."""
        self.resource = resource or boto3.resource("s3")
        self._bucket = self.resource.Bucket(self.NAME)

    def upload_html_file(self, path):
        """Uploads a static HTML file to the bucket, given its path.

        Args:
            path: str
        """
        self._bucket.upload_file(
            Filename=path,
            Key=path.split("/")[-1],
            ExtraArgs={"ContentType": "text/html"},
        )


class SiteGenerator:
    """Generates HTML files and stores them in the site bucket."""

    CURRENT_WEEK_PATH = "/tmp/current.html"  # noqa: S108
    PREVIOUS_WEEK_PATH = "/tmp/previous.html"  # noqa: S108

    def __init__(self, table, renderer, bucket):
        """Initialise with dependencies.

        Args:
            table: DataTable
            renderer: HtmlRenderer
            bucket: S3Bucket
        """
        self._table = table
        self._renderer = renderer
        self._bucket = bucket

    def _write_html_to_file(self, path, content):
        """Write the rendered HTML string to a file at given path.

        Args:
            path: str
            content: str
        """
        with open(path, "w+", encoding="utf-8") as file:
            file.write(content)

    def generate(self):
        """Generate the site and store the HTML files in the bucket."""
        LOGGER.info(
            "Generating site for current week %s", self._table.current_season_week
        )
        self._write_html_to_file(
            self.CURRENT_WEEK_PATH, self._renderer.render_current_week()
        )
        self._bucket.upload_html_file(self.CURRENT_WEEK_PATH)

        if previous := self._renderer.render_previous_week():
            LOGGER.info(
                "Generating site for previous week %s", self._table.previous_season_week
            )
            self._write_html_to_file(self.PREVIOUS_WEEK_PATH, previous)
            self._bucket.upload_html_file(self.PREVIOUS_WEEK_PATH)
