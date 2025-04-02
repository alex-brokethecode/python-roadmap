# List Comprehension vs. Loop: Write a Python program that uses the timeit module to compare the execution time
# of creating a list of squares using a list comprehension versus a for loop.

import timeit


def list_comprehension(n: int):
    return [i ** 2 for i in range(1, n + 1)]


def loop(n: int):
    output = []
    for i in range(1, n+1):
        output.append(i ** 2)

    return output


def test(n: int):
    lc_time = timeit.timeit(
        stmt=f'list_comprehension({n})',
        setup='from __main__ import list_comprehension',
        number=1
    )

    l_time = timeit.timeit(
        stmt=f'loop({n})',
        setup='from __main__ import loop',
        number=1
    )

    print(f'For a list of {n} numbers')
    print(f'List Comprehension time: {lc_time}')
    print(f'Loop time: {l_time}')


if __name__ == '__main__':
    test(1000000)
