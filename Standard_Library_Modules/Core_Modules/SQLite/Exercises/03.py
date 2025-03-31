# Update and Delete: Write a Python program that updates and deletes data in an SQLite database table based on given conditions

import sqlite3

with sqlite3.connect('db.sqlite') as conn:
    try:
        cursor = conn.cursor()

        # Update
        cursor.execute('UPDATE test SET name = ? WHERE id = ?', ('Jaime', 1))
        # cursor.rowcount after UPDATE/DELETE operations will return the number of rows affected (0, n)

        if cursor.rowcount == 0:
            print('No rows updated')
        else:
            # cursor.rowcount after SELECT operation will return -1
            cursor.execute('SELECT * FROM test')
            print(cursor.fetchall())

        # Delete
        cursor.execute('DELETE FROM test WHERE id = ?', (1,))

        if cursor.rowcount == 0:
            print('No rows deleted')
        else:
            cursor.execute('SELECT * FROM test')
            print(cursor.fetchall())

        conn.commit()

    except sqlite3.Error as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: {e}')
