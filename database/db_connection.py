import sqlite3
from sqlite3 import Error as Err

def get_db_connection(schemafile: str = 'database/schema.sql'):
    """Run the schema file to create the database with the table and return the connection."""
    
    conn = None
    try:
        conn = sqlite3.connect('database.db')
        print("Connection established successfully")
        

        if schemafile:
            with open(schemafile, 'r') as f:
                schema = f.read()
                conn.row_factory = sqlite3.Row 
            cursor = conn.cursor()
            cursor.executescript(schema)
            conn.commit()
            cursor.close()

            print("Schema applied successfully")

    except Err as e:
        print(f"An error occurred: {e}")
    return conn