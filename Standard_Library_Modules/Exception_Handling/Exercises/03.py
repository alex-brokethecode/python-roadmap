# Custom Exception for Invalid Input: Create a custom exception class called InvalidInputError. Write a Python program that takes a number as input and raises InvalidInputError if the number is negative.

class InvalidInputError(Exception):
    def __init__(self, number: int, message: str = 'Invalid input.') -> None:
        self.number = number
        super().__init__(message)


def ask_number():
    if (number := int(input('Enter number: '))) < 0:
        raise InvalidInputError(number, 'Only positive numbers are allowed.')

    return number


try:
    number = ask_number()
    print(number)
except InvalidInputError as e:
    print(f'Error: {e} {e.number} is a negative number')
