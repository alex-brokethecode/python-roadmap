# `os` Module

## Theory

The `os` module provides a portable way of using operating system-dependent functionality. It allows you to interact with the operating system, such as working with files and directories, running commands, and accessing environment variables.

### File and Directory Operations

- `os.getcwd()`: Returns the current working directory.
- `os.chdir(path)`: Changes the current working directory.
- `os.listdir(path)`: Returns a list of the entries in the directory given by path.
- `os.mkdir(path)`: Creates a directory.
- `os.makedirs(path)`: Creates directories recursively.
- `os.rmdir(path)`: Removes a directory.
- `os.remove(path)`: Removes a file.
- `os.path.join(path1, path2, ...)`: Joins path components intelligently.
- `os.path.exists(path)`: Checks if a path exists.
- `os.path.isfile(path)`: Checks if a path is a file.
- `os.path.isdir(path)`: Checks if a path is a directory.
- `os.walk(path)`: Generates file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (root, dirs, files).

  - `root` is a string, the path to the directory.
  - `dirs` is a list of the names of the subdirectories in root (excluding '.' and '..').
  - `files` is a list of the names of the non-directory files in root.

### Running Commands

- `os.system(command)`: Executes a shell command.

### Environment Variables

`os.environ`: A dictionary-like object that provides access to environment variables.

### Example

```python
import os

# Current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# List files in directory
files = os.listdir(cwd)
print("Files in directory:", files)

# Create a directory
os.makedirs("my_new_dir/subdir", exist_ok=True)

# Join paths
file_path = os.path.join("my_new_dir", "subdir", "my_file.txt")
print("Joined path:", file_path)

# Check if path exists
if os.path.exists(file_path):
    print("Path exists")

# Environment variables
print("Home directory:", os.environ.get("HOME"))
```

## Exercises:

### Easy

1. **List Files:** Write a Python program that takes a directory path as input and prints a list of all files and directories in that path. [Solution](./Exercises/01.py)

### Medium

2. **Create and Remove Directories:** Write a Python program that takes a directory path as input, creates the directory (and any necessary parent directories), and then removes the directory (if it's empty). [Solution](./Exercises/02.py)

### Hard

3. **Find Files by Extension:** Write a Python program that takes a directory path and a file extension as input and prints a list of all files in that directory (and its subdirectories) that have the specified extension. [Solution](./Exercises/03.py)
