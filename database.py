import mysql.connector
import numpy as np


class DataBase:

    def __init__(self, config):
        sql_data = config.getMySqlCredentials()

        self.connection = mysql.connector.connect(
            host=sql_data['host'],
            user=sql_data['user'],
            auth_plugin=sql_data['auth_plugin'],
            password=sql_data['password'],
            database=sql_data['database']
        )

        self.config_data = config

    def getTableData(self):
        query = self.config_data.getQuery()
        cursor = self.connection.cursor()
        cursor.execute(query)

        return {
            'column_names': cursor.column_names,
            'table_data': np.array(cursor.fetchall())
        }
