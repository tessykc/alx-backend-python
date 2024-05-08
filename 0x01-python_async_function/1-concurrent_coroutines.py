#!/usr/bin/env python3

import asyncio
from typing import List

from 0x01_python_async_function import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: Sorted list of delay times.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed, _ = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    return sorted([task.result() for task in completed])


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
