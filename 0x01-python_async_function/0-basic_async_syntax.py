#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return the delay time."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    # Run the coroutine and print the result
    print(await wait_random())
    print(await wait_random(5))
    print(await wait_random(15))
