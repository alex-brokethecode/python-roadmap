# Topic: Asynchronous Programming (asyncio)

## Theory

Asynchronous programming allows you to run multiple tasks concurrently without them blocking each other. This is achieved using event loops and coroutines.

- **Event Loop:** The heart of `asyncio`. It manages and schedules the execution of asynchronous tasks.
- **Coroutines:** Functions defined with `async def`. They can pause their execution using `await` and yield control back to the event loop.
- **`await` Keyword:** Used inside coroutines to pause the execution of the coroutine until the awaited operation (e.g., an I/O operation) is complete.
- **Tasks:** Coroutines can be wrapped in `asyncio.Task` objects to schedule their execution on the event loop.
- **`asyncio.run()`:** A convenient function to run the top-level entry point of an asyncio program. It creates and manages the event loop.

**Example 1:**

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'first')
    await say_after(2, 'second')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

You can create a task from a coroutine using `asyncio.create_task()`. This function takes a coroutine as an argument and schedules it to run concurrently with other tasks on the event loop.

**Example 2:**

```python
import asyncio
import time

async def say_after(delay, message) -> None:
    await asyncio.sleep(delay)
    print(message, time.strftime('%X'))


async def main() -> None:
    task1 = asyncio.create_task(say_after(2, 'Hello'))
    task2 = asyncio.create_task(say_after(3, 'Bye'))

    print(f'Started at {time.strftime('%X')}')

    await task1
    await task2

    print(f'Finished at {time.strftime('%X')}')


asyncio.run(main()) # Between 3 seconds both coroutines run concurrently
```

## Exercises:

### Easy

1. **Simple Async Function:** Create an asynchronous function that prints a message after a short delay using asyncio.sleep(). [Solution](./Exercises/01.py)

### Medium

2. **Concurrent Tasks:** Write a program that runs two or more asynchronous tasks concurrently using asyncio.create_task(). [Solution](./Exercises/02.py)

### Hard

3. **Asynchronous Web Request:** Use the aiohttp library to make an asynchronous HTTP GET request to a website and print the response status code. [Solution](./Exercises/03.py)
