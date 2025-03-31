# Create and Insert: Write a Python program that creates an SQLite database, creates a table and inserts some sample data into the table

import sqlite3

try:
    with sqlite3.connect('db.sqlite') as conn:
        cursor = conn.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)')
        cursor.execute('INSERT INTO test (name) VALUES (?)', ('John',))
        cursor.execute('INSERT INTO test (name) VALUES (?)', ('Megan',))

        conn.commit()

        cursor.execute('SELECT * FROM test')
        rows = cursor.fetchall()

    print(rows)
except sqlite3.OperationalError as e:
    print(f'Operational error: {e}')
except sqlite3.IntegrityError as e:
    print(f'Integrity error: {e}')
except sqlite3.DatabaseError as e:
    print(f'Database error: {e}')
except sqlite3.Error as e:
    print(f'General SQLite error: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
