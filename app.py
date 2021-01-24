import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import sqlite3

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

conn = sqlite3.connect('data/database.db')

server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = pd.read_sql_query(
        '''
        select season, week, date ||' '|| time as date_time, teama_name, teamh_name, score
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

app.layout = html.Div(
    style={'width': '800px',
    'font-family': 'Courier',
    'margin': 'auto'
    }
    
    , children=[
    
    html.H1('''
    Which NFL game from last week was the most fun to watch?'''
    , style={'textAlign': 'center'})
    
    , html.Br()

    , html.Div('''
    Without giving away the score or the winner, 
    this app ranks games from the 2020 season by a fun index
    that accounts for closeness, points, yards and turnovers.
    ''')
    
    , html.Br()
    
    , html.Div('''
    Don't waste your time watching a snoozefest!
    ''')
    
    , html.Br()

    , dcc.Dropdown(
        id = 'season_drop',
        options=drop_seasons,
        value=[current_season],
        multi=True
    )  

    , html.Br()

    , dcc.Dropdown(
        id = 'week_drop',
        options=drop_weeks,
        value=[current_week],
        multi=True
    )  
    , html.Br()
    , html.Br()

    , dash_table.DataTable(
        id='data',
        columns=[{'name': i, 'id': i} for i in data.columns],
        data=data.to_dict('records'),
        style_as_list_view=True,
        style_cell={'padding': '5px'}
        )
    
    , html.Br()
    , html.Br()
    , html.Br()
    , html.Br()
    ])

###############################
# WORK IN PROGRESS

@app.callback(
    Output('filtered_table', 'table'),
    Input('season_drop', 'value'),
    Input('season_drop', 'value')
)
def update_table(selected_season, selected_week):
    filtered_df = df[df.season == selected_season && df.week == selected_week]

###############################


if __name__ == '__main__':
    app.server.run(debug=True, threaded=True, host='0.0.0.0')