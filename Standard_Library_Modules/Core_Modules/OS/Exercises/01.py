# List Files: Write a Python program that takes a directory path as input
# and prints a list of all files and directories in that pat

import os


def list_files(path: str = '.') -> None:
    for file in os.listdir(path):
        print(file)


list_files('../')
