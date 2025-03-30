# Serialize to JSON: Write a Python program that takes a dictionary as input and serializes it to a JSON formatted string

import json


def obj_to_json(obj: dict) -> str:
    return json.dumps(obj, indent=4)


data = {
    'name': 'John Doe',
    'gender': 'male',
    'age': 24
}

try:
    json_str = obj_to_json(data)
    print(json_str)
except Exception as e:
    print(f'Error: {e}')
