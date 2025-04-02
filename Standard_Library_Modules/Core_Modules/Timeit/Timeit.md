# `timeit` Module

## Theory

The `timeit` module provides a simple way to time small bits of Python code. It's useful for measuring the execution time of different code snippets and comparing their performance.

- `timeit.timeit(stmt, setup, timer, number, globals)`:
  - `stmt`: The statement to be timed (a string).
  - `setup`: Code to be executed before the statement (a string).
  - `timer`: A timer function (optional).
  - `number`: The number of times to execute the statement.
  - `globals`: A dictionary of global variables (optional).
- `timeit.repeat(stmt, setup, timer, repeat, number, globals)`:
  - Similar to `timeit.timeit()`, but returns a list of results from multiple executions.
  - `repeat`: The number of times to repeat the timing.
- `timeit.default_timer()`:
  - A platform-specific timer function.

## Example

```python
import timeit

# Time the execution of a simple statement
time_taken = timeit.timeit(
    stmt="[i**2 for i in range(100)]",
    number=10000
)

print(f"Time taken: {time_taken} seconds")

# Time the execution of a function
def my_function(n: int):
    return [i**2 for i in range(n)]

time_taken = timeit.timeit(
    stmt="my_function(100)",
    setup="from __main__ import my_function",
    number=10000
)

print(f"Time taken: {time_taken} seconds")

# Using repeat
times = timeit.repeat(
    stmt="[i**2 for i in range(100)]",
    number=1000,
    repeat=5
)

print(f"Times: {times}")
print(f"Best time: {min(times)} seconds")
```

## Exercises:

### Easy

1. **List Comprehension vs. Loop:** Write a Python program that uses the timeit module to compare the execution time of creating a list of squares using a list comprehension versus a for loop. [Solution](./Exercises/01.py)

### Medium

2. **String Concatenation:** Write a Python program that uses the timeit module to compare the execution time of string concatenation using the + operator versus the join() method. [Solution](./Exercises/02.py)

### Hard

3. **Function Call Overhead:** Write a Python program that uses the timeit module to measure the overhead of calling a simple function repeatedly. [Solution](./Exercises/03.py)
