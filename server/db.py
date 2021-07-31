import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error
import enum

def __create_server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv('HOST_NAME'),
            user=os.getenv('USER_NAME'),
            passwd=os.getenv('PASSWORD')
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def get_connection():
    connection = __create_server_connection()
    return connection

q1 = """
SELECT * FROM GroceryApp.super_market_view;
"""

def select_all(table):
    return f""" 
    SELECT * FROM GroceryApp.{table}
    """

class view_tables(enum.Enum):
   super_market_view = "super_market_view" 
   recipe_view = "recipe_view"