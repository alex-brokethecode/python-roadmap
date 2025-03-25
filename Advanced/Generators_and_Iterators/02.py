# Fibonacci Generator: Create a generator function that yields the Fibonacci sequence up to a given limit

def generate_fibonacci(limit: int):
    if limit < 0:
        raise ValueError('n must be a positive integer.')

    if not isinstance(limit, int):
        raise TypeError('n must be an integer.')

    a, b = 0, 1

    while a <= limit:
        yield a
        a, b = b, a + b


try:
    for num in generate_fibonacci(10):
        print(num)
except Exception as e:
    print(e)
