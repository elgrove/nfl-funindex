import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import pandas as pd
import sqlite3
from time import sleep

conn = sqlite3.connect('data/database.db')
cursor = conn.cursor()
from data.gridiron_scraper.scraper import updateDB

updateDB(cursor)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = pd.read_sql_query(
        '''
        select season
        , week
        , date ||' '|| time as date_time
        , teama_name
        , teamh_name
        , score
        from game_score
        order by season asc, week asc, score desc;
        '''
        , conn)

seasons = set([i for i in data.season])
weeks = set([i for i in data.week])
drop_seasons = [{'label' : i, 'value' : i} for i in seasons]
current_season = max(seasons)
drop_weeks = [{'label' : i, 'value' : i} for i in weeks]
current_week = data[data.season == data.season.max()].week.max()

data.score = data.score.map('{:,.2f}'.format)
data.columns = ['Season', 'Week', 'Date', 'Away', 'Home', 'Fun Index']
data = data.sort_values('Date', ascending = True)
#data.Date = pd.to_datetime(data.Date)

current = data[(data.Season == current_season) & (data.Week == current_week)]
rest = data[(data.Season == current_season) & (data.Week != current_week)]



app.layout = html.Div(
    style={'width': '800px',
    'font-family': 'Trebuchet MS',
    'font-size' : '110%',
    'margin': 'auto'
    }

    , children=[

    html.Br()
   
    , html.H1('''
    Which NFL game from last week was the most fun to watch?'''
    , style={'textAlign': 'center'})
    
    , html.Br()

    , html.Div('''
    The NFL Fun Index uses standard data points like points, yards and turnovers,
     as well as taking into account game state, big plays and dramatic moments 
     to take the decision of which game to watch out of your hands - all without giving away the scores!
    ''')
    
    , html.Br()

    , html.Div('''
    Last week:
    ''')
    
    , html.Br()

    , dash_table.DataTable(
        id='current',
        columns=[{'name': i, 'id': i} for i in current.columns],
        data=current.to_dict('records'),
        style_as_list_view=True,
        style_cell={'padding': '5px',
        'textAlign' : 'center'},
        sort_action='native'
        #filter_action='native'

        )

    , html.Br()

    , html.Div('''
    The rest of this season:
    '''
    )

    , html.Br()

    , dash_table.DataTable(
        id='rest',
        columns=[{'name': i, 'id': i} for i in rest.columns],
        data=rest.to_dict('records'),
        style_as_list_view=True,
        style_cell={'padding': '5px'},
        sort_action='native'
        #filter_action='native'

        )

    , html.Br()
    , html.Br()
    ])




if __name__ == '__main__':
    app.server.run(debug=True, threaded=True, host='0.0.0.0')


