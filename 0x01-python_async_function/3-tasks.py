import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int):
    """Return an asyncio.Task that will run the wait_random coroutine."""
    return asyncio.create_task(wait_random(max_delay))

# Example usage in your 3-main.py:
if __name__ == "__main__":
    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
