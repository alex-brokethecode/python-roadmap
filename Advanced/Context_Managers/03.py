# Database Connection Context Manager: Create a context manager that manages a database connection, ensuring it is properly opened and closed

import sqlite3


class DatabaseConnection:
    """Manages a database connection."""

    def __init__(self, db_name: str):
        self.db_name = db_name

    def __enter__(self):
        """Opens a database connection."""
        self.conn = sqlite3.connect(self.db_name)
        print(f'Connected to {self.db_name}')
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        """Closes the database connection and commits changes."""
        if exc_type:
            self.conn.rollback()
            print('Transaction rolled back due to exception.')
        else:
            self.conn.commit()
            print('Transaction committed.')

        self.conn.close()
        print(f'Connection closed')


with DatabaseConnection('db.sqlite') as conn:
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO test (name) VALUES (?)', ('example',))
