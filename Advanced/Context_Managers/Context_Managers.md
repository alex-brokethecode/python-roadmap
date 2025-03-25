# Context Managers

## Theory

Context managers are used to manage resources, ensuring they are properly set up and torn down. The most common use case is with the with statement.

- `__enter__()` and `__exit__()` Methods:

  - A class can become a context manager by implementing the `__enter__()` and `__exit__()` methods.
  - `__enter__()` is called when the with block is entered. It can return a value that will be assigned to the target of the as clause in the `with` statement.
  - `__exit__(exc_type, exc_value, traceback)` is called when the `with` block is exited. It can handle exceptions that occur within the `with` block.

    - `exc_type`: This parameter holds the exception type if an exception occurred within the with block.
    - `exc_value`: This parameter holds the exception instance if an exception occurred.

    - `traceback`: This parameter holds a traceback object that encapsulates information about where the exception occurred.

- `contextlib` Module:
  - The `contextlib` module provides utilities for creating and working with context managers.
  - `contextlib.contextmanager` decorator: This decorator allows you to create context managers using generator functions.

**Example:**

```python
# Context Manager Class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# Context Manager Usage
with FileManager('example.txt', 'w') as f:
    f.write('Hello, Context Managers!')
```

```python
# Context Manager with contextlib
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with file_manager('example2.txt', 'w') as f:
    f.write('Hello, Contextlib!')
```

### Comparison

Before context managers became widely used, working with files often involved manually opening and closing them. This could lead to issues if the file wasn't closed properly, especially in case of exceptions.

```python
# Without Context Manager
file = open('example.txt', 'w')
try:
    file.write('Hello, files!')
finally:
    file.close()
```

With Context Managers:

- Automatic Closing: The with statement automatically closes the file, even if exceptions occur.
- Conciseness: This approach is more concise and readable.
- Safety: It ensures that the file is always closed, preventing resource leaks.

```python
# With Context Manager
with open('example.txt', 'w') as file:
    file.write('Hello, Context Managers!')
```

## Exercises

### Easy

1. **Timer Context Manager:** Create a context manager that measures and prints the execution time of a code block. [Solution](./Exercises/01.py)

### Medium

2. **Change Directory Context Manager:** Create a context manager that temporarily changes the current working directory. [Solution](./Exercises/02.py)

### Hard

3. **. Database Connection Context Manager:** Create a context manager that manages a database connection, ensuring it is properly opened and closed. [Solution](./Exercises/03.py)
