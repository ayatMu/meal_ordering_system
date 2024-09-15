from database.db_connection import get_db_connection
import sqlite3


def execute_query(query: str, params: tuple = ()):
    # TODO: Implement this function
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        conn.close()

        return "Query executed successfully"
    except sqlite3.Error as e:
        return f"An error occurred: {e}"


def fetch_data(query: str, params: tuple = ()):
    # TODO: Implement this function
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        data = cursor.fetchall() 
        cursor.close()
        conn.close()

        return data
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
