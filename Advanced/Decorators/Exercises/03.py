# Retry Decorator: Create a decorator that retries a function a specified number of times if it raises an exception


def retry(times: int = 3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f'Attempt {i + 1}')
                try:
                    result = func(*args, **kwargs)
                    return result  # Return result if successful
                except Exception as e:
                    print(f'Retry failed: {e}')
            # Raise exception if all retries fail
            raise Exception(f'Function failed after {times} retries')
        return wrapper
    return decorator


@retry()
def convert_to_int(value: str) -> int:
    if not value.isnumeric():
        raise ValueError(f'"{value}" is not numeric')

    return int(value)


try:
    result = convert_to_int('x')
    print(result)
except Exception as e:
    print(e)
