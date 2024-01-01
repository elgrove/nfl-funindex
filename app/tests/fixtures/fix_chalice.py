"""Test fixtures for the Chalice app."""
from app import app
from chalice.test import Client
import pytest


@pytest.fixture(name="client")
def chalice_client():
    """Fixture for invoking Chalice endpoints."""
    return Client(app)
