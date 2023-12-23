import pytest
from jinja2 import Template

from chalicelib.site_generator import HtmlRenderer
from chalicelib.table import DataTable
from tests.cases.case_renderer import WEEK_1_GAMES_RENDERED, WEEK_2_GAMES_RENDERED


@pytest.mark.unit
class TestHtmlRenderer:
    def test_template(self, data_table_week_1):
        """Given a data table containing games

        When the template is rendered into a html string

        Then it is an instance of a jinja2.Template
        """
        table = DataTable(table=data_table_week_1)
        template = HtmlRenderer(table)._template
        assert isinstance(template, Template)

    def test_render_current_week(self, data_table_weeks_1_2):
        """Given a data table containing weeks 1 and 2

        When the current week is rendered

        Then it contains all the games from week 2.
        """
        table = DataTable(table=data_table_weeks_1_2)
        renderer = HtmlRenderer(table)
        rendered = renderer.render_current_week()
        assert WEEK_2_GAMES_RENDERED in rendered

    def test_render_previous_week_yes(self, data_table_weeks_1_2):
        """Given a data table containing weeks 1 and 2

        When the previous week is rendered

        Then it contains all the games from week 1.
        """
        table = DataTable(table=data_table_weeks_1_2)
        renderer = HtmlRenderer(table)
        rendered = renderer.render_previous_week()
        assert WEEK_1_GAMES_RENDERED in rendered

    def test_render_previous_week_no(self, data_table_week_1):
        """Given a data table containing week 1 only

        When the previous week is rendered

        Then it contains all the games from week 2.
        """
        table = DataTable(table=data_table_week_1)
        renderer = HtmlRenderer(table)
        assert renderer.render_previous_week() is None
