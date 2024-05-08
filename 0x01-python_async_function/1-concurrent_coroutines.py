#!/usr/bin/env python

import asyncio
import random

from ./0x01-python_async_function import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Spawn wait_random n times with the specified max_delay."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed, _ = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    # Extract the results from completed tasks and return them
    return [task.result() for task in completed]


# Example 
if __name__ == "__main__":
    asyncio.run(wait_n(5, 5))
    asyncio.run(wait_n(10, 7))
    asyncio.run(wait_n(10, 0))
