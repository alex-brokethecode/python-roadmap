# `argparse` Module

## Theory

The `argparse` module makes it easy to write user-friendly command-line interfaces. It allows you to define the arguments that your script can accept and provides help messages to guide users.

- `argparse.ArgumentParser()`: Creates an argument parser object.
- `parser.add_argument(name_or_flags, ...)`: Adds an argument to the parser.
- `parser.parse_args()`: Parses the command-line arguments.

### Argument Types

- Positional arguments: Required arguments that are specified by their position.
- Optional arguments: Arguments that are specified by flags (e.g., `-h`, `--help`).

### Argument Actions

- `store`: Stores the argument value.
- `store_true`: Stores `True` if the argument is present.
- `store_false`: Stores `False` if the argument is present.
- `count`: Counts the number of times the argument is present.
- `append`: Appends the argument value to a list.

### Argument Data Types

- `type=int`: Specifies that the argument should be an integer.
- `type=float`: Specifies that the argument should be a float.
- `type=str`: Specifies that the argument should be a string.

### Help Messages

- `help="message"`: Specifies a help message for the argument.

### Example

```python
import argparse

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "integers", # name of the positional argument
    metavar="N", # name that will be display in help message
    type=int, # argument should be converted to an integer
    nargs="+", # accept one or more values
    help="an integer for the accumulator"
    )
parser.add_argument(
    "--sum", # flag to use to specify the argument
    dest="accumulate", # name of the attribute that will be added to args object
    action="store_const", # argument should store a constant value
    const=sum, # constant value that should be stored if the argument is present (sum)
    default=max, # default value that should be stored if the argument is not present (max)
    help="sum the integers (default: find the max)"
    )

args = parser.parse_args() # returns an Namespace object containing the parsed values
print(args.accumulate(args.integers))
```

## Exercises:

### Easy

1. **Simple Argument:** Write a Python program that takes a string argument from the command line and prints it. [Solution](./Exercises/01.py)

### Medium

2. **Integer Arguments:** Write a Python program that takes two integer arguments from the command line and prints their sum. [Solution](./Exercises/02.py)

### Hard

3. **File Input and Output:** Write a Python program that takes an input file path and an output file path as arguments. The program should read the contents of the input file, convert the contents to uppercase, and write the uppercase contents to the output file. [Solution](./Exercises/03.py)
