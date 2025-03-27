# Generate Squares: Create a generator function that yields the squares of numbers from 0 to n.

def generate_squares(n: int):
    for i in range(n + 1):
        yield i ** 2


for square in generate_squares(3):
    print(square)
