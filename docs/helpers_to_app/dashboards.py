from dash import Dash, html, dcc, Input, Output, dash_table
from .create_table_and_graphs import Graphs, Table_func_create
import dash_bootstrap_components as dbc


class create_dashboards:
    @staticmethod
    def create_basic_dashboards(year):
        return dbc.Container([
            dbc.Row([
                dbc.Col(dcc.Graph(id='religion_yishuv',
                                  figure=Graphs.religion_yishuv(year=year)), md=4),
                dbc.Col(dcc.Graph(id='yishuvim type',
                                  figure=Graphs.type_yishuv(year=year)), md=4),
                dbc.Col(dcc.Graph(id='jewish/arabic pop',
                                  figure=Graphs.jewish_and_arabic_pop(year=year)), md=4)
            ], className="h-25 g-0"),
            dbc.Row(children="Table of data",style={'textAlign': 'center'}),
            dbc.Row([
                dbc.Col(
                    Table_func_create.table_technical_settlement_information(year=year),
                    width=12
                )
            ], className="h-25 g-0"),

            dbc.Row([
                dbc.Col(dcc.Graph(id='avg. height',
                                  figure=Graphs.avg_height(year=year))),
                dbc.Col(dcc.Graph(id='construct_comitee',
                                  figure=Graphs.construct_comitee(year=year))
                        )
            ], className="h-25 g-0")
        ], fluid=True)
