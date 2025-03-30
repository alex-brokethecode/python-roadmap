# requests Module

## Theory

The `requests` module is a powerful and widely used library for making HTTP requests in Python. It simplifies the process of sending HTTP requests and handling responses, making it essential 1 for web scraping, interacting with APIs, and other web-related tasks.

- `requests.get(url)`: Sends a GET request to the specified URL.
- `requests.post(url, data)`: Sends a POST request to the specified URL with the given data.
- `requests.put(url, data)`: Sends a PUT request to the specified URL with the given data.
- `requests.delete(url)`: Sends a DELETE request to the specified URL.
- `response.status_code`: The HTTP status code of the response (e.g., 200 for OK, 404 for Not Found).
- `response.text`: The content of the response as a string.
- `response.json()`: The content of the response as a JSON object (if the response is in JSON format).
- `response.headers`: The HTTP headers of the response.
- `response.raise_for_status()`: Raises an HTTPError if the response status code indicates an error.

### Sending Data

Data can be sent as a dictionary (for form data) or as a JSON string.

### Handling Errors

- Use `response.raise_for_status()` to check for HTTP errors.
- Use `try...except` blocks to handle network errors or other exceptions.

### Example

```python
import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    data = response.json()
    print("Data:", data)

    response = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "foo", "body": "bar", "userId": 1})
    response.raise_for_status()

    print("Post Response: ", response.json())

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

## Exercises

### Easy

1. **Get Request:** Write a Python program that sends a GET request to a specified URL and prints the response text. [Solution](./Exercises/01.py)

### Medium

2. **JSON Data:** Write a Python program that sends a GET request to a JSON API endpoint, parses the JSON response, and prints a specific field from the JSON data. [Solution](./Exercises/02.py)

### Hard

3. **Post Request:** Write a Python program that sends a POST request to an API endpoint with JSON data and prints the JSON response from the server. [Solution](./Exercises/03.py)
