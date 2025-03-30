# Find Files by Extension: Write a Python program that takes a directory path and a file extension as input
# and prints a list of all files in that directory (and its subdirectories) that have the specified extension

import os


def find_files_by_extension(path: str, extension: str) -> None:
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))


find_files_by_extension('.', 'md')
