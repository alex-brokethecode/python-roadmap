# `json` Module

## Theory

The `json` module provides a way to encode and decode JSON (JavaScript Object Notation) data in Python. JSON is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.

- `json.dumps(obj)`: Serializes a Python object to a JSON formatted string.
- `json.loads(json_str)`: Deserializes a JSON formatted string to a Python object.
- `json.dump(obj, file_obj)`: Serializes a Python object to a JSON formatted stream to a file.
- `json.load(file_obj)`: Deserializes a JSON formatted stream from a file to a Python object.

### Python to JSON Conversion:

- dict -> object
- list, tuple -> array
- str -> string
- int, float -> number
- True -> true
- False -> false
- None -> null

### JSON to Python Conversion:

- object -> dict
- array -> list
- string -> str
- number -> int, float
- true -> True
- false -> False
- null -> None

### Example

```python
import json

# Python object
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Serialize to JSON string
json_str = json.dumps(data, indent=4)
print("JSON string:", json_str)

# Deserialize from JSON string
python_obj = json.loads(json_str)
print("Python object:", python_obj)

# Write to JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read from JSON file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print("Loaded data:", loaded_data)
```

## Exercises

### Easy

1. **Serialize to JSON:** Write a Python program that takes a dictionary as input and serializes it to a JSON formatted string.

### Medium

2. **Deserialize from JSON:** Write a Python program that takes a JSON formatted string as input and deserializes it to a Python dictionary.

### Hard

3. **Read and Write JSON File:** Write a Python program that reads data from a JSON file, modifies the data (e.g., adds a new key-value pair), and writes the modified data back to the same JSON file.
