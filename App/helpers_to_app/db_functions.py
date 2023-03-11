import json

import mysql.connector
import pandas as pd

class func_to_db:
    @staticmethod
    def connect_to_db():
        with open('C:\\Users\\User\\PycharmProjects\\Population analysis\\config.json'
                  ) as f:
            config = json.load(f)
        mydb = mysql.connector.connect(**config)
        return mydb
    @staticmethod
    def run_sql_query_to_df(sql_query):
        mydb = func_to_db.connect_to_db()
        return pd.read_sql_query(sql=sql_query, con=mydb)
