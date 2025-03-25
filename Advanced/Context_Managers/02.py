# Change Directory Context Manager: Create a context manager that temporarily change the current working directory

from pathlib import Path
from os import chdir


class ChangeDirectory:
    def __init__(self, new_directory):
        self.new_directory = Path(new_directory)
        self.original_directory = Path.cwd()

    def __enter__(self):
        chdir(self.new_directory)
        return self.new_directory

    def __exit__(self, exc_type, exc_value, traceback):
        chdir(self.original_directory)


with ChangeDirectory('../'):
    print(f'Inside Context Manager: {Path.cwd()}')

print(f'Outside Context Manager: {Path.cwd()}')
