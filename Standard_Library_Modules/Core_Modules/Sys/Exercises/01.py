# Command-Line Argument Echo: Write a Python program that takes command-line arguments and prints them to the console

import sys

# fmt: off
sum = lambda x, y: x + y 

# fmt: on
if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])

            print(f'First argument: {a}')
            print(f'Second argument: {b}')
            print(f'Sum: {sum(a, b)}')
        except ValueError:
            print('The 2 arguments must be integer numbers')
    else:
        print('Please pass 2 integer arguments after the filename')
