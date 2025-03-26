# Concurrent Tasks: Write a program that runs two or more asynchronous tasks concurrently using asyncio.create_task().

import asyncio
import time


async def say(message: str, delay: int) -> None:
    await asyncio.sleep(delay)
    print(f'{message} after {delay} seconds')


async def main() -> None:
    task1 = asyncio.create_task(say('Task 1', 3))
    task2 = asyncio.create_task(say('Task 2', 1))
    task3 = asyncio.create_task(say('Task 3', 2))

    print(f'Started at {time.strftime('%X')}')

    await task1
    await task2
    await task3

    print(f'Finished at {time.strftime('%X')}')


asyncio.run(main())
