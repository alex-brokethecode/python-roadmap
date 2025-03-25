# Time Context Manager: Create a context manager that measures and prints the execution time of a code block

import time


def count_numbers(n: int) -> None:
    for _ in range(n):
        pass


class TimeManager:
    def __enter__(self):
        self.start_time = time.time()
        return self  # Return self, as there's no specific resource to return

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        print(f'Execution time: {self.end_time - self.start_time} seconds')


with TimeManager() as tm:
    count_numbers(1000000)
