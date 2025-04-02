# Function Call Overhead: Write a Python program that uses the timeit module to measure
# the overhead of calling a simple function repeatedly

import timeit


def empty_function():
    pass  # This function does nothing


def empty_loop():
    for _ in range(1000000):
        pass


def test(times: int):
    function_time = timeit.timeit(
        stmt="empty_function()",
        setup="from __main__ import empty_function",
        number=times,
    )

    loop_time = timeit.timeit(
        stmt="empty_loop()",
        setup="from __main__ import empty_loop",
        number=1,
    )

    print(f"Time for {times} empty function calls: {function_time}")
    print(f"Time for empty loop: {loop_time} seconds")

    print(f"Function call overhead: {function_time - loop_time}")


if __name__ == '__main__':
    test(1000000)
