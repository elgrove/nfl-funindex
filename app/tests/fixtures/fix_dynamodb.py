import boto3
import pytest
from moto import mock_dynamodb


def create_tables(resource):
    """Creates mock versions of the nfl-data table."""
    table_definition = {
        "TableName": "nfl-data",
        "AttributeDefinitions": [
            {"AttributeName": "id", "AttributeType": "S"},
            {"AttributeName": "season_week", "AttributeType": "S"},
        ],
        "KeySchema": [
            {"AttributeName": "id", "KeyType": "RANGE"},
            {"AttributeName": "season_week", "KeyType": "HASH"},
        ],
        "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        "BillingMode": "PROVISIONED",
    }
    resource.create_table(**table_definition)


@pytest.fixture
def data_table():
    """Fixture returning empty DynamoDB table.

    Yields:
        dynamodb.Table
    """
    with mock_dynamodb():
        resource = boto3.resource("dynamodb")
        create_tables(resource)
        data_table = resource.Table("nfl-data")
        data_table.meta.client.get_waiter("table_exists").wait(TableName="nfl-data")
        yield data_table


@pytest.fixture
def data_table_week_1(data_table, previous_week_1_games):
    """Fixture returning a DynamoDB table with week 1 data.

    Yields:
        dynamodb.Table
    """
    with data_table.batch_writer() as batch:
        for game in previous_week_1_games:
            batch.put_item(Item=game)
    yield data_table


@pytest.fixture
def data_table_weeks_1_2(data_table, games_data):
    """Fixture returning a DynamoDB table with week 1 and 2 data.

    Yields:
        dynamodb.Table
    """
    with data_table.batch_writer() as batch:
        for game in games_data:
            batch.put_item(Item=game)
    yield data_table
