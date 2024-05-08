#!/usr/bin/env python3

import asyncio
from typing import List

# Import wait_random from the previous file
from 0x01_python_async_function import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]


if __name__ == "__main__":
    asyncio.run(wait_n(5, 5))
    asyncio.run(wait_n(10, 7))
    asyncio.run(wait_n(10, 0))
    
