# JSON Data: Write a Python program that sends a GET request to a JSON API endpoint, parses the JSON response,
# and prints a specific field from the JSON data.

import requests
import json

url = 'https://reqres.in/api/users'


def get_user_info(user_id: int) -> dict | None:
    try:
        response = requests.get(f'{url}/{user_id}')
        response.raise_for_status()

        return response.json()['data']
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None


user = get_user_info(2)

if user:
    json_str = json.dumps(user, indent=4)
    print(json_str)
    print('Email:', user.get('email', 'N/A'))
else:
    print('User not found')
