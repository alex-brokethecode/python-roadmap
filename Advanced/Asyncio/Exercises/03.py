# Asynchronous Web Request: Use the aiohttp library to make an asynchronous HTTP GET request to a website and print the response status code

import aiohttp
import asyncio


async def fetch_url(url: str) -> None:
    async with aiohttp.ClientSession() as session:  # Create a session
        try:
            async with session.get(url) as response:  # Request
                print(f'Fetching "{url}"')
                print('Status:', response.status)
                text = await response.text()
                print('Text:', text[:100])
        except aiohttp.ClientError as e:
            print(f'Error fetching {url}: {e}')


async def main() -> None:
    urls = [
        'http://www.python.org',
        'https://www.google.com'
    ]

    # Create coroutines
    tasks = [fetch_url(url) for url in urls]

    # Instead of awaiting each task individually (await task1, await task2), asyncio.gather() allows you to launch them all and then wait for all of them to finish in a single await call.
    await asyncio.gather(*tasks)

asyncio.run(main())


# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://python.org') as response:
#             print('Status:', response.status)
#             html = await response.text()
#             print('Body:', html[:15], "...")


# asyncio.run(main())
