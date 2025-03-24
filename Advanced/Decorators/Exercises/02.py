# Logging Decorator: Create a decorator that logs the input arguments and return value of a function


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(
            f'Calling {func.__name__} function with args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} function returned: {result}')
        return result

    return wrapper


@logging_decorator
def add(a, b):
    return a + b


print(add(1, 3))
