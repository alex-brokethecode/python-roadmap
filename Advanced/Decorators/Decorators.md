# Topic: Decorators

## Theory

Decorators in Python are essentially functions that wrap other functions, adding functionality or modifying their behavior. They use the `@` symbol, also known as the "at" symbol, followed by the decorator's name.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

In this example, my_decorator adds extra functionality before and after the say_hello function is called.

## Key Concepts

- **First-class functions:** Functions can be passed as arguments to other functions.
- **Inner functions:** Functions can be defined inside other functions.
- **Closures:** Inner functions can access variables from their enclosing scope.

## Exercises

### Easy

1. **Timing Decorator:** Create a decorator that measures and prints the execution time of a function. [Solution](./Exercises/01.py)

### Medium

2. **Logging Decorator:** Create a decorator that logs the input arguments and return value of a function. [Solution](./Exercises/02.py)

### Hard

3. **Retry Decorator:** Create a decorator that retries a function a specified number of times if it raises an exception. [Solution](./Exercises/03.py)
