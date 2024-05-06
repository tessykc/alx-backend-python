#!/usr/bin/env python3


import asyncio
from asyncio import tasks4-tasks.py

from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """Call task_wait_random n times with the specified max_delay."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

# Example usage in your 4-main.py:
if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
