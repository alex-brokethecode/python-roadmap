# Working with Files (I/O)

## Theory

Python provides built-in functions for reading from and writing to files. The `open()` function is the primary way to interact with files.

- **Opening Files:**
  - `open(filename, mode)`: Opens a file and returns a file object.
  - `filename`: The name of the file to open.
  - `mode`: A string specifying the mode in which the file should be opened. Common modes include:
    - `'r'`: Read mode (default). Opens the file for reading.
    - `'w'`: Write mode. Opens the file for writing. If the file exists, it is truncated (delete all existing content and size to zero). If it doesn't exist, it is created.
    - `'a'`: Append mode. Opens the file for writing. Data written will be appended to the end of the file. If the file doesn't exist, it is created.
    - `'x'`: Exclusive creation mode. Opens the file for writing only if it doesn't exist. If it exists, it raises a `FileExistsError`.
    - `'b'`: Binary mode (can be combined with other modes, e.g., `'rb'`, `'wb'`).
    - `'+'`: Opens a file for updating (reading and writing).
- **Reading from Files:**
  - `file.read()`: Reads the entire content of the file as a single string.
  - `file.readline()`: Reads a single line from the file.
  - `file.readlines()`: Reads all lines from the file and returns them as a list of strings.
  - With these methods, the file pointer moves forward. To reread the file content, can close and reopen the file or use `file.seek(0)`.
- **Writing to Files:**
  - `file.write(string)`: Writes a string to the file.
  - `file.writelines(list_of_strings)`: Writes a list of strings to the file.
- **Closing Files:**
  - `file.close()`: Closes the file. It's important to close files after you're done with them to release system resources.
- **Using `with` Statement (Recommended):**
  - The `with` statement is the preferred way to work with files as it ensures that the file is properly closed even if exceptions occur.

```python
with open('my_file.txt', 'r') as f:
    content = f.read()
    print(content)

with open('output.txt', 'w') as f:
    f.write('Hello, world!')
```

- Can combine some modes: The most common combination is using `'r+'` or `'w+'`.
  - `'r+'` (Read and Write): Opens the file for both reading and writing. The file pointer is initially at the beginning of the file. If the file doesn't exist, it raises a `FileNotFoundError`.
  - `'w+'` (Write and Read): Opens the file for both writing and reading. If the file exists, it's truncated. If it doesn't exist, it's created. The file pointer is initially at the beginning.

## Exercises

### Easy

1.  **Read a File:** Write a Python program that reads the content of a file named `sample.txt` (you'll need to create this file with some text) and prints its content to the console. [Solution](./Exercises/01.py)

### Medium

2.  **Write to a File:** Write a Python program that takes a string as input and writes it to a new file named `output.txt`. [Solution](./Exercises/02.py)

### Hard

3.  **File Reader with Error Handling:** Write a Python program that attempts to read a file specified by the user. Implement error handling to catch `FileNotFoundError` if the file does not exist and print an informative message. [Solution](./Exercises/03.py)
