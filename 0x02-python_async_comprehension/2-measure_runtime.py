#!/usr/bin/env python3

import asyncio
import time
from 1-async_comprehension import async_comprehension


async def measure_runtime():
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time: end_time - start_time
