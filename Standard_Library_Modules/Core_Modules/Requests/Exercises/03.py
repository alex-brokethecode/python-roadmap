# Post Request: Write a Python program that sends a POST request to an API endpoint with JSON data and prints the JSON response from the server

import requests
import json

URL = 'https://reqres.in/api/users/'


def create_user(data: dict) -> None:
    try:
        response = requests.post(URL, data)
        response.raise_for_status()

        if response.status_code == 201:
            json_str = json.dumps(response.json(), indent=4)
            print(json_str)
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')


data = {
    "name": "morpheus",
    "job": "leader"
}

create_user(data)
