# Get Request: Write a Python program that sends a GET request to a specified URL and prints the response text

import requests

ENDPOINT = 'https://api.lyrics.ovh/v1'


def search_lyrics(artist: str, title: str) -> str | None:
    artist = artist.strip()
    title = title.strip()

    try:
        response = requests.get(f'{ENDPOINT}/{artist}/{title}')
        response.raise_for_status()

        if response.status_code == 200:
            return response.json()['lyrics']

        return None

    except requests.exceptions.HTTPError as e:
        print(f'HTTP Error: {e}')
        return None
    except requests.exceptions.ConnectionError as e:
        print(f'Connection Error: {e}')
        return None
    except requests.exceptions.Timeout as e:
        print(f'Timeout Error: {e}')
        return None
    except Exception as e:
        print(f'An unexpected error occurred {e}')
        return None


lyrics = search_lyrics('nemo', 'the code')

if lyrics:
    print(lyrics)
else:
    print('Lyrics not found or an error occurred')
