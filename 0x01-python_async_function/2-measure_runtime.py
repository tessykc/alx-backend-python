#!/usr/bin/env python


import asyncio
import time
from previous_file import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n and return the average time per call."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

# Example usage in your 2-main.py:
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
