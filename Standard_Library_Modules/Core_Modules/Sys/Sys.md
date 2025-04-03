# `sys` Module

## Theory

The `sys` module provides access to system-specific parameters and functions. It allows you to interact with the Python interpreter and the operating system environment.

- Command-Line Arguments (`sys.argv):

  - `sys.argv` is a list of command-line arguments passed to a Python script.
  - The first element (`sys.argv[0]`) is the script's name
  - Subsequent elements are the arguments provided by the user.

- Exiting the Program (`sys.exit()`):

  - `sys.exit()` terminates the Python program.
  - You can provide an optional exit code as an argument.
  - A zero exit code (e.g., `sys.exit(0)`) typically indicates successful execution.
  - A non-zero exit code (e.g., `sys.exit(1)`) typically indicates an error.

- Standard Input/Output/Error (`sys.stdin`, `sys.stdout`, `sys.stderr`):

  - `sys.stdin` is a file-like object representing standard input (e.g., keyboard input).
  - `sys.stdout` is a file-like object representing standard output (e.g., console output).
  - `sys.stderr` is a file-like object representing standard error output (e.g., error messages).

- Python Path (`sys.path`):

  - `sys.path` is a list of strings that specifies the search path for modules.
  - You can modify `sys.path` to add directories to the module search path.

- Python Version (`sys.version`):

  - `sys.version` is a string containing information about the Python interpreter's version.

- Platform Information (`sys.platform`):

  - `sys.platform` is a string containing the platform identifier (e.g., `"win32"`, `"linux"`, `"darwin"`).

## Example

```python
import sys

print(f"Script name: {sys.argv[0]}")
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")

if len(sys.argv) > 1:
    print("Arguments:")
    for arg in sys.argv[1:]:
        print(arg)

try:
    user_input = input("Enter something: ")
    print(f"You entered: {user_input}")
except KeyboardInterrupt:
    print("\nKeyboardInterrupt caught!")
    sys.exit(1)
```

## Exercises

### Easy

1. **Command-Line Argument Echo:** Write a Python program that takes command-line arguments and prints them to the console. [Solution](./Exercises/01.py)

### Medium

2. **Modify Python Path:** Write a Python program that takes a directory path as a command-line argument and adds it to the Python module search path (sys.path). [Solution](./Exercises/02.py)

### Hard

3. **Platform-Specific Output:** Write a Python program that prints a different message depending on the operating system platform (e.g., Windows, Linux, macOS). [Solution](./Exercises/03.py)
