#!/usr/bin/env python3

import asyncio
from 0-async_generator import async_generator


async def async_comprehension():
    return [i async for i in async_generator()]: [i async for i in async_generator()]
