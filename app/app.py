"""Entry point for Chalice app."""
import logging
import os

from chalice import Chalice

from chalicelib.checker import Checker
from chalicelib.publisher import EventPublisher
from chalicelib.schedule import Schedule
from chalicelib.scraper import GameScraper, GameScraperDirector
from chalicelib.site_generator import HtmlRenderer, S3Bucket, SiteGenerator
from chalicelib.table import DataTable

app = Chalice(app_name="nfl")

LOGGER = app.log
LOGGER.setLevel(logging.INFO)


@app.schedule("rate(2 hours)")
def checker(_event):
    """Checks source for new games to scrape, puts the IDs onto EventBridge if found."""
    checker_ = Checker(DataTable(), Schedule(), EventPublisher())
    checker_.check()


@app.lambda_function()
def checker_manual(_event, _context):
    """As with checker but can be manually triggered, is not dependent on an event."""
    checker_ = Checker(DataTable(), Schedule(), EventPublisher())
    checker_.check()


@app.on_cw_event({"detail-type": ["game_to_scrape"]})
def game_scraper(event):
    """Listens for game IDs to scrape, computes fun index and puts data to DynamoDB."""
    game_id = event.to_dict()["detail"]["id"]
    director = GameScraperDirector(DataTable(), GameScraper(game_id))
    director.scrape()


@app.on_dynamodb_record(os.environ["DATA_TABLE_STREAM"])
def site_generator(_event):
    """Listens for changes to the DynamoDB table and re-generates the static site."""
    table = DataTable()
    renderer = HtmlRenderer(table)
    gen = SiteGenerator(table, renderer, S3Bucket())
    gen.generate()
