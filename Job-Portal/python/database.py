
# File: python/database.py

import mysql.connector
from mysql.connector import Error


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234567890@",
    "port": "3306",
    "database": "job_portal_db"
}


def get_connection():
    """Create and return a MySQL database connection."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            return connection

    except Error as error:
        print(f"Database connection failed: {error}")

    return None

