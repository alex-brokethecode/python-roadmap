# Prime Number Generator: Create a generator function that yields prime numbers indefinitely.

def is_prime(n: int):
    if n <= 1:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


def generate_primes():
    num = 2

    while True:
        if is_prime(num):
            yield num
        num += 1


primes_generator = generate_primes()

for i in range(10):
    print(next(primes_generator))
