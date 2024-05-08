#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return the delay time."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# If you want to use this coroutine in your 0-main.py, you can do so like this:

if __name__ == "__main__":
    # Import the coroutine
    from ./0x01-python_async_function import wait_random

    # Run the coroutine and print the result
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
