# Create and Remove Directories: Write a Python program that takes a directory path as input,
# creates the directory (and any necessary parent directories), and then removes the directory (if it's empty)

import os
import time


def create_and_remove_dir(path: str) -> None:
    try:
        os.makedirs(path, exist_ok=True)
        print(f'{path} created successfully')

        time.sleep(3)

        os.removedirs(path)  # remove only empty dirs
        print(f'{path} removed successfully')
    except Exception as e:
        print(f'Error: {e}')


create_and_remove_dir('./new_dir/sub_dir')
