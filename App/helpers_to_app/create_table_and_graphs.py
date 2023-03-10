import json

import mysql.connector
import pandas as pd
from dash import Dash, html, dcc, Input, Output, dash_table
import plotly.express as px
from .db_functions import func_to_db


class Table_func_create:
    @staticmethod
    def table_technical_settlement_information(year):
        mydb = func_to_db.connect_to_db()
        sql_query = f"select * from technical_settlement_information where year_data={year}"
        df = pd.read_sql_query(sql=sql_query, con=mydb)
        table = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], id='tbl')
        return table


class Graphs:
    @staticmethod
    def avg_height(year):
        mydb = func_to_db.connect_to_db()
        sql_query = f"select average_height from technical_settlement_information where year_data={year}"
        df = pd.read_sql_query(sql=sql_query, con=mydb)
        hist_height = px.histogram(data_frame=df, x='average_height',title="Avg. Height")
        return hist_height
    @staticmethod
    def religion_yishuv(year):
        mydb = func_to_db.connect_to_db()
        sql_query = f"SELECT tsi.name_of_settlements, tsi.religion_code, rc.explanation " \
                    f"FROM technical_settlement_information tsi " \
                    f"JOIN religions_code rc ON tsi.religion_code = rc.religion_code " \
                    f"WHERE year_data = {year}"
        df = pd.read_sql_query(sql=sql_query, con=mydb)
        pie = px.pie(df, values='religion_code', names='explanation', title="Settlements according to major religion")
        return pie

