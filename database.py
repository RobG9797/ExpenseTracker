import sqlite3

DB_NAME = "expenses.db"

def initialise_database():
    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL,
            cost_pence INTEGER NOT NULL,
            category TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()