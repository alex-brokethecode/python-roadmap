# Integer Arguments: Write a Python program that takes two integer arguments from the command line and prints their sum

# Usage: py main.py number_1 number_2 [--multiply]

import argparse

parser = argparse.ArgumentParser(description='Sum two integers')

# nargs = creates a list. If you don't specifies, you can directly sum values
parser.add_argument(
    'number_1',
    metavar='N1',
    type=int,
    help='The first number'
)
parser.add_argument(
    'number_2',
    metavar='N2',
    type=int,
    help='The second number'
)
parser.add_argument(
    '--multiply',
    action='store_true',  # Stores true if the argument is present
    help='Multiply the numbers instead of summing them'
)

args = parser.parse_args()

try:
    if args.multiply:
        print(args.number_1 * args.number_2)
    else:
        print(args.number_1 + args.number_2)
except AttributeError:
    print('Error: Please provide two integer arguments')
