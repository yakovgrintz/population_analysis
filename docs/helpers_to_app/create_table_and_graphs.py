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
        table = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],
                                     page_size=100,
                                     style_table={'height': '100%', 'overflowY': 'auto'}, virtualization=True

                                     )
        return table


class Graphs:
    @staticmethod
    def avg_height(year):
        sql_query = f"select average_height from technical_settlement_information where year_data={year}"
        df = func_to_db.run_sql_query_to_df(sql_query)
        hist_height = px.histogram(data_frame=df, x='average_height', title="Avg. Height", template="ggplot2")
        return hist_height

    @staticmethod
    def religion_yishuv(year):
        sql_query = f"SELECT tsi.name_of_settlements, tsi.religion_code, rc.explanation " \
                    f"FROM technical_settlement_information tsi " \
                    f"JOIN religions_code rc ON tsi.religion_code = rc.religion_code " \
                    f"WHERE year_data = {year}"
        df = func_to_db.run_sql_query_to_df(sql_query)
        pie = px.pie(df, values='religion_code', names='explanation', title="Settlements according to major religion",
                     template="ggplot2")
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
                             title="Planning and construction councils (if there is data)", color='name',
                             template="ggplot2")
        return scatter

    @staticmethod
    def jewish_and_arabic_pop(year):
        sql_query = f" SELECT SUM(jewish_pop),SUM(arabic_pop)" \
                    f" FROM technical_settlement_information" \
                    f" WHERE year_data = {year}"
        df = func_to_db.run_sql_query_to_df(sql_query=sql_query)
        pie = px.pie(df, values=[df['SUM(jewish_pop)'].iloc[0], df['SUM(arabic_pop)'].iloc[0]],
                     names=['Jewish Pop', 'Arabic Pop'], title='The distribution of the population Jews/Arabs',
                     template="ggplot2")
        return pie

    @staticmethod
    def type_yishuv(year):
        sql_query = f"SELECT tsi.Type_of_settlement as type_code  ,ts.type,ts.type_yishuv " \
                    f"FROM technical_settlement_information tsi " \
                    f"JOIN type_of_settlement ts ON tsi.Type_of_settlement = ts.type_code " \
                    f"WHERE year_data = {year}"
        df = func_to_db.run_sql_query_to_df(sql_query)
        pie = px.pie(data_frame=df, values='type_code', names='type', color='type_yishuv'
                     , title="Type Of Yishuvim", template="ggplot2")
        pie.update_traces(textposition='inside')
        pie.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', showlegend=False)

        return pie

    @staticmethod
    def found_year(year):
        return None
