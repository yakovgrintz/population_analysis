import json
import mysql.connector
from dash import Dash, html, dcc, Input, Output, dash_table,State
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from helpers_to_app.create_table_and_graphs import Table_func_create
from helpers_to_app.create_table_and_graphs import Graphs
from helpers_to_app.db_functions import func_to_db

# connect to db
mydb = func_to_db.connect_to_db()
# options to drop down year
year_query = "select distinct year_data from technical_settlement_information"
cursor = mydb.cursor()
cursor.execute(year_query)
options = [{'label': row[0], 'value': row[0]} for row in cursor.fetchall()]
mydb.close()
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
app.layout = html.Div(children=[
    html.H1(children='Population Analysis Dashboard', style={'textAlign': 'center'}),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    html.Div(id='select data to present', style={'textAlign': 'center'}, children=[
        dcc.Dropdown(
            id='select year',
            options=options
        ),
        html.Div(id='table of data')

    ]),
    html.Div(id='Graph of data')
])


@app.callback(Output('table of data', 'children'),
               Input('select year', 'value')
              )
def update_data_and_Graph(value):

    return Table_func_create.table_technical_settlement_information(value)
@app.callback(Output('Graph of data', 'children'),
               Input('select year', 'value'))
def update_graph_data(value):
    children = [
        dcc.Graph(id='avg. height',
                  figure=Graphs.avg_height(value)),
        dcc.Graph(id='religion_yishuv',
                  figure=Graphs.religion_yishuv(value))
    ]
    return children


if __name__ == '__main__':
    app.run_server(debug=True)
