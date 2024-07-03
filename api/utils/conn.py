import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()


db_config = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'database': os.getenv("DB_DATABASE"),
    'port':os.getenv('DB_PORT'),
    'ssl_ca': 'api/mysql.cert'
}





def get_connection():

    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            return conn
    except Exception as e:
        return e

