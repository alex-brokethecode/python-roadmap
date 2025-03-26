# Simple Async Function: Create an asynchronous function that prints a message after a short delay using asyncio.sleep()

import time
import asyncio


async def tell(message: str, delay: int) -> None:
    """Prints a message after a specified delay."""
    # Coroutine
    await asyncio.sleep(delay)
    print(f'> {message} at', time.strftime('%X'))


async def main() -> None:
    """Runs the asynchronous tasks."""
    print('Started at:', time.strftime('%X'))
    await tell('Hello', 2)
    await tell('Bye', 3)


asyncio.run(main())
