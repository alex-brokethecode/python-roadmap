# Read and Write JSON File: Write a Python program that reads data from a JSON file, modifies the data (e.g. adds a new key-value pair),
# and write the modified data back to the same JSON file

import json


def read_json_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'Error: File {file_path} not found.')
        return {}


def write_json_file(file_path: str, obj: dict) -> None:
    with open(file_path, 'w') as file:
        json.dump(obj, file)


filename = 'data.json'

try:

    obj = read_json_file(filename)

    if obj:
        obj['language'] = 'English'
        write_json_file(filename, obj)
        print(read_json_file(filename))
except Exception as e:
    print(f'Error: {e}')
