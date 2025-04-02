# `random` Module

## Theory

The random module provides functions for generating pseudo-random numbers. These functions can be used for a wide variety of applications, such as simulations, games, and security.

- `random.random()`: Returns a random float between 0 and 1.
- `random.randint(a, b)`: Returns a random integer between a and b (inclusive).
- `random.choice(seq)`: Returns a random element from the sequence seq.
- `random.shuffle(seq)`: Shuffles the sequence seq in place.
- `random.seed(x)`: Initializes the random number generator.
- `random.uniform(a, b)`: Returns a random float between a and b (inclusive).
- `random.sample(population, k)`: Returns a k length list of unique elements chosen from the population sequence.

> [!NOTE]
>
> - `secrets` is a more specialized module for security-critical applications, while `random` is a more general-purpose module for non-security-critical applications.
> - `secrets` can be considered a more robust and secure version of some of the functionalities that the `random` module has.

## Example

```python
import random

# Generate a random float between 0 and 1
print(random.random())

# Generate a random integer between 1 and 10
print(random.randint(1, 10))

# Choose a random element from a list
my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))

# Shuffle a list in place
random.shuffle(my_list)
print(my_list)
```

## Exercises

### Easy

1. **Dice Roll:** Write a Python program that simulates rolling a six-sided die. [Solution](./Exercises/01.py)

### Medium

2. **Random Password Generator:** Write a Python program that generates a random password of a specified length. [Solution](./Exercises/02.py)

### Hard

3. **Card Shuffling and Dealing:** Write a Python program that simulates shuffling a deck of cards and dealing a hand of a specified number of cards. [Solution](./Exercises/03.py)
