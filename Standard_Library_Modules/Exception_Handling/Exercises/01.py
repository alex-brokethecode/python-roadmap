# Divide by Zero: Write a Python program that takes two numbers as input and divides the first number by the second. Handle the ZeroDivisionError exception and print an appropriate message

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero.')

    return a / b


try:
    print(divide(28, 7))
    print(divide(28, 0))
except ZeroDivisionError as e:
    print(f'Error: {e}')

# Custom Exception


class DivisionByZeroException(Exception):
    def __init__(self, a, b, message="Don't do it.") -> None:
        self.a = a
        self.b = b
        super().__init__(message)


def run_divide(a, b):
    if b == 0:
        raise DivisionByZeroException(a, b)

    return a / b


try:
    print(run_divide(28, 7))
    print(run_divide(28, 0))
except DivisionByZeroException as e:
    print(f'Error: {e} Cannot divide {e.a} by {e.b}')
