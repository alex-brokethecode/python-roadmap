# String Concatenation: Write a Python program that uses the timeit to compare
# the execution time of string concatenation using the + operator versus the join() method

from string import ascii_lowercase
import timeit

letters = list(ascii_lowercase)


def concatenation():
    output = ''
    for letter in letters:
        output += letter

    return output


def join_method():
    return ''.join(letters)


def test(number: int, repeat: int):
    c_time = timeit.repeat(
        stmt='concatenation()',
        setup='from __main__ import concatenation',
        number=number,
        repeat=repeat
    )
    j_time = timeit.repeat(
        stmt='join_method()',
        setup='from __main__ import join_method',
        number=number,
        repeat=repeat
    )

    print(f'For number={number} and repeat={repeat}')
    print(f'Concatenation time: {c_time}')
    print(f'Join time: {j_time}')


if __name__ == '__main__':
    test(100000, 5)
