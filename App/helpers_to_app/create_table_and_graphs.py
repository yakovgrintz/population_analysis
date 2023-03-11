import json

import mysql.connector
import pandas as pd
from dash import Dash, html, dcc, Input, Output, dash_table
import plotly.express as px
from .db_functions import func_to_db


class Table_func_create:
    @staticmethod
    def table_technical_settlement_information(year):
        sql_query = f"select * from technical_settlement_information where year_data={year}"
        df = func_to_db.run_sql_query_to_df(sql_query)
        table = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], id='tbl',
                                     page_size=20)
        return table


class Graphs:
    @staticmethod
    def avg_height(year):
        sql_query = f"select average_height from technical_settlement_information where year_data={year}"
        df = func_to_db.run_sql_query_to_df(sql_query)
        hist_height = px.histogram(data_frame=df, x='average_height', title="Avg. Height")
        return hist_height

    @staticmethod
    def religion_yishuv(year):

        sql_query = f"SELECT tsi.name_of_settlements, tsi.religion_code, rc.explanation " \
                    f"FROM technical_settlement_information tsi " \
                    f"JOIN religions_code rc ON tsi.religion_code = rc.religion_code " \
                    f"WHERE year_data = {year}"
        df = func_to_db.run_sql_query_to_df(sql_query)
        pie = px.pie(df, values='religion_code', names='explanation', title="Settlements according to major religion")
        return pie

    @staticmethod
    def construct_comitee(year):
        sql_query = f"SELECT count(tsi.code_yishuv) as Count_Of_Yishuvin, tsi.Construction_Planning_Committee,sum(tsi.population) as Sum_Of_Pop ,cc.name ,cc.type " \
                    f"FROM technical_settlement_information tsi " \
                    f"JOIN construction_planning_committee cc ON tsi.Construction_Planning_Committee = cc.code_committee " \
                    f"WHERE year_data = {year}" \
                    f" GROUP BY tsi.Construction_Planning_Committee"
        df = func_to_db.run_sql_query_to_df(sql_query)
        scatter = px.scatter(data_frame=df, x='Count_Of_Yishuvin', y='Sum_Of_Pop',
                             title="Planning and construction councils (if there is data)", color='name')
        return scatter
    @staticmethod
    def jewish_and_arabic_pop(year):
        return None
    @staticmethod
    def type_yishuv(year):
        return None
    @staticmethod
    def found_year(year):
        return None
