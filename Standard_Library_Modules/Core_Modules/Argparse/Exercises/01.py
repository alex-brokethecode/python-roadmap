# Simple Argument: Write a Python program that takes a string argument from the command line a prints it.

# Usage: py main.py name

import argparse

# Create parser object
parser = argparse.ArgumentParser(description='Greets with the passed name')
# Positional argument
parser.add_argument(
    'name',  # name of argument
    metavar='NAME',  # displayed name in command help
    type=str,  # convert to type
    nargs=1,  # number of parameters
    help='string to print'  # help message
)

# namespace object containing parsed values
args = parser.parse_args()
print(f'Hello {args.name[0]}')
