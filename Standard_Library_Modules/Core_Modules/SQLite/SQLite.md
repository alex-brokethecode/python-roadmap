# sqlite3 Module

## Theory

The `sqlite3` module provides a lightweight disk-based database that doesn't require a separate server process and allows you to access SQLite databases using a SQL-compliant interface. SQLite is a self-contained, high-reliability, embedded, full-featured, public-domain, SQL database engine.

- `sqlite3.connect(database_path)`: Creates a connection to an SQLite database.
- `connection.cursor()`: Creates a cursor object to execute SQL queries.
- `cursor.execute(sql_query, parameters)`: Executes an SQL query with optional parameters.
- `cursor.fetchone()`: Fetches the next row of a query result.
- `cursor.fetchall()`: Fetches all rows of a query result.
- `connection.commit()`: Saves changes to the database.
- `connection.close()`: Closes the database connection.

### SQL Queries

- `CREATE TABLE table_name (column1 datatype, column2 datatype, ...)`: Creates a table.
- `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...)`: Inserts data into a table.
- `SELECT column1, column2, ... FROM table_name WHERE condition`: Retrieves data from a table.
- `UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition`: Updates data in a table.
- `DELETE FROM table_name WHERE condition`: Deletes data from a table.

### Example

```python
import sqlite3

# Connect to database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
conn.commit()

# Retrieve data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Rows:", rows)

# Close connection
conn.close()
```

## Exercises:

### Easy

1. Create and Insert: Write a Python program that creates an SQLite database, creates a table, and inserts some sample data into the table. [Solution](./Exercises/01.py)

### Medium

2. Retrieve Data: Write a Python program that retrieves data from an SQLite database table based on a given condition and prints the results. [Solution](./Exercises/02.py)

### Hard

3. Update and Delete: Write a Python program that updates and deletes data in an SQLite database table based on given conditions. [Solution](./Exercises/03.py)
