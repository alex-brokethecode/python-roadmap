# Random Password Generator: Write a Python program that generates a random password of a specified length.

# from random import choice
from secrets import choice
from string import ascii_letters, digits, punctuation


def generate_password(length: int) -> str:
    characters = ascii_letters + digits + punctuation

    return ''.join(choice(characters) for _ in range(length))


print(generate_password(15))
