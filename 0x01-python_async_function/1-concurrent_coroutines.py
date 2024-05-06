#!/usr/bin/env python


import asyncio
import random

# Assuming wait_random is defined in another file as before
from your_module_name import wait_random

async def wait_n(n: int, max_delay: int) -> list:
    """Spawn wait_random n times with the specified max_delay."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed, _ = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    # Extract the results from completed tasks and return them
    return [task.result() for task in completed]

# Example usage in your 1-main.py:
if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
