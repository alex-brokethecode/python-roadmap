# Retrieves Data: Write a Python program that retrieves data from an SQLite database table based on a given condition
# and prints the results

import sqlite3

try:
    with sqlite3.connect('db.sqlite') as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM test WHERE name = ?', ('Megan',))
        result = cursor.fetchone()

        print(result)
except sqlite3.Error as e:
    print(f'Error: {e}')
except Exception as e:
    print(f'Error: {e}')
