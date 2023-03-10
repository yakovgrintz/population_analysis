import json

import mysql.connector

class func_to_db:
    @staticmethod
    def connect_to_db():
        with open('C:\\Users\\User\\PycharmProjects\\Population analysis\\config.json'
                  ) as f:
            config = json.load(f)
        mydb = mysql.connector.connect(**config)
        return mydb
