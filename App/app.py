from dash import Dash, html, dcc, Input, Output, dash_table, State
import dash_bootstrap_components as dbc

from App.helpers_to_app.dashboards import create_dashboards
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
    html.H1(children=' Israel Population Analysis Dashboard', style={'textAlign': 'center'}),
    html.P(["Welcome to my dashboard.", html.Br(),
            "This dashboard will present & analyze data from CBS of israel.", html.Br(),
            "please select year of data to start:"], style={'textAlign': 'center'}),

    html.Div(id='select data to present', style={'textAlign': 'center'}, children=[
        dcc.Dropdown(
            id='select year',
            options=options
        ),
        html.Div(id='basic dashboard', style={'textAlign': 'center', 'width': '100%', 'height': '100%'})

    ]),

])


@app.callback(Output('basic dashboard', 'children'),
              Input('select year', 'value')
              )
def update_basic_dashboard(value):
    return create_dashboards.create_basic_dashboards(value)


if __name__ == '__main__':
    app.run_server(debug=True)
