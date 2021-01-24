'''Instantiate a Dash app.'''
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import numpy as np
import pandas as pd
import sqlite3

from .layout import html_layout

def init_dashboard(server):
    '''Create a Plotly Dash dashboard.'''
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/2020/',
        external_stylesheets=[
            'https://fonts.googleapis.com/css?family=Lato',
        ],
    )
    conn = sqlite3.connect('/home/aaron/new-nfl-site/flask_app/dash/database.db')
    
    latest = pd.read_sql_query(
        '''
        select week, date ||' '|| time as date_time, teama_name, teamh_name, score
        from game_score 
        where season = 2020 
        and week = (
            select max(week) from game_score
            ) 
        order by score desc;
        '''
        , conn)

    secondLatest = pd.read_sql_query(
        '''
        select week, date ||' '|| time as date_time, teama_name, teamh_name, score
        from game_score 
        where season = 2020 
        and week = (
            select max(week)-1 from game_score
            ) 
        order by score desc;
        '''
        , conn)

    others = pd.read_sql_query(
        '''
        select week, date ||' '|| time as date_time, teama_name, teamh_name, score
        from game_score 
        where season = 2020 
        and week != (
            select max(week) from game_score
            ) 
        and week != (
            select max(week)-1 from game_score
            ) 
        order by week desc, score desc;
        '''
        , conn)


    # Custom HTML layout
    dash_app.index_string = html_layout

    dash_app.layout = html.Div(
        style={'width': '800px',
        'font-family': 'Courier',
        'margin': 'auto'
        }
        , children=[
        html.Br()
        , html.Br()

        , create_data_table(latest, '1')

        , html.Br()
        , html.Br()

        , create_data_table(secondLatest, '2')

        , html.Br()
        , html.Br()

        , create_data_table(others, '3')

        , html.Br()
        , html.Br()
        , html.Br()
        , html.Br()

    ])


    return dash_app.server


def create_data_table(df, id):
    df.score = df.score.round(1)
    df.columns = [
        'Week'
        , 'Time'
        , 'Away Team'
        , 'Home Team'
        ,'Fun Index'
    ]
    df['Time'] = pd.to_datetime(df.Time)
    '''Create Dash datatable from Pandas DataFrame.'''
    table = dash_table.DataTable(
        id=f'database-table-{id}',
        columns=[{'name': i, 'id': i} for i in df.columns],
        data=df.to_dict('records'),
        style_as_list_view=True,
        style_cell={'padding': '5px'},
        sort_action='native',
        sort_mode='native',
        page_size=300,
    )
    return table
