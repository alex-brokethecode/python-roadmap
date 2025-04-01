# File Input and Output: Write a Python program that takes an input file path and an output file path as arguments
# The program should read the contents of the input file, convert the contents to uppercase, and write the uppercase contents to the output file

import argparse

parser = argparse.ArgumentParser(
    description='Read a file and write the uppercase version to other file')

# If argument has spaces, the parse_args returns a dict, else returns a Namespace(key, value)
parser.add_argument(
    'input_file',
    metavar='INPUT FILE',
    type=str,
    help='The name of the input file'
)
parser.add_argument(
    'output_file',
    metavar='OUTPUT FILE',
    type=str,
    help='The name of the output file'
)

try:
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    with open(input_file, 'r') as file:
        content = file.read()

    with open(output_file, 'w+') as file:
        file.write(content.upper())
        file.seek(0)
        content = file.read()
        print(content)
except AttributeError:
    print('Error: Please enter two strings for input and output files')
except FileNotFoundError:
    print('Error: File not found')
except Exception as e:
    print(f'Error: {e}')
