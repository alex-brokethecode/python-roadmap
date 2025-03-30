# Deserialize from JSON: Write a Python program that takes a JSON formatted string as input
# and deserializes it to a Python dictionary

import json


def json_to_obj(json_str: str) -> dict:
    return json.loads(json_str)


data = '{"name": "John Doe", "gender": "male", "age": 24}'

try:
    obj = json_to_obj(data)
    print(obj)
except Exception as e:
    print(f'Error: {e}')
