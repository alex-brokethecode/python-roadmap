# Timing Decorator: Create a decorator that measures and prints the execution time of a function

import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):  # Flexibility at retrieving parameters
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Total execution time: {end_time - start_time} seconds')
        return result  # Return the result of the decorated function

    return wrapper


@timing_decorator
def count_numbers(n: int) -> list[int]:
    return [i for i in range(n)]


numbers = count_numbers(1000)
print(numbers)
