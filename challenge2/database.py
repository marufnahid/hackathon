import sqlite3
from config import DATABASE_PATH

# Function to execute SQL queries
def execute_query(query, args=()):
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()

# Function to fetch SQL query results
def fetch_query(query, args=()):
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(query, args)
        return cursor.fetchall()

# Initialize the database schema for ingredients and recipes
def init_db():
    # Create ingredients table
    query = """
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        quantity TEXT NOT NULL
    );
    """
    execute_query(query)

    # Create recipes table
    query = """
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        taste TEXT,
        reviews TEXT,
        cuisine TEXT,
        preparation_time TEXT,
        recipe_text TEXT
    );
    """
    execute_query(query)
