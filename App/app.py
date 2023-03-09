import json
import mysql.connector
from dash import Dash, html, dcc, Input, Output,dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from helpers_to_app.create_table_and_graphs import Table_func_create

# connect to db
with open('../config.json') as f:
    config = json.load(f)
mydb = mysql.connector.connect(**config)
# options to drop down year
year_query = "select distinct year_data from technical_settlement_information"
cursor = mydb.cursor()
cursor.execute(year_query)
options = [{'label': row[0], 'value': row[0]} for row in cursor.fetchall()]
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
app.layout = html.Div(children=[
    html.H1(children='Population Analysis Dashboard', style={'textAlign': 'center'}),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    html.Div(id='select data to present',style={'textAlign': 'center'},children=[
        dcc.Dropdown(
            id='select year',
            options=options
        ),
        html.Div(id='table of data')

    ])
])
@app.callback(Output('table of data','children'),Input('select year','value'))
def update_table(value):
    sql_query = f"select * from technical_settlement_information where year_data={value}"
    df = pd.read_sql_query(sql=sql_query, con=mydb)
    return dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], id='tbl')
if __name__ == '__main__':
    app.run_server(debug=True)
