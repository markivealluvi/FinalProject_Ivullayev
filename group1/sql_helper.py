from aifc import Error
import mysql.connector as mysql


class MySQL:
    @staticmethod
    def create_connection():
        connection = None
        try:
            connection = mysql.connect(host="127.0.0.1",
                                       user="root",
                                       passwd="",
                                       database="litecart")
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    @staticmethod
    def execute_read_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    @staticmethod
    def close_db(connection):
        connection.close()
        print("Database closed")

    query_orders = 'SELECT * FROM `lc_orders`'
    query_customers = 'SELECT firstname FROM `lc_customers`'
