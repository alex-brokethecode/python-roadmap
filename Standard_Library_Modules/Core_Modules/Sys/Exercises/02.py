# Modify Python Path: Write a Python program that takes a directory path as a command-line argument
# and adds it to the Python module search path (sys.path)


import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        sys.exit(1)

    # Add the directory to sys.path
    sys.path.append(directory_path)

    print(f"Added {directory_path} to sys.path")
    print(sys.path)
