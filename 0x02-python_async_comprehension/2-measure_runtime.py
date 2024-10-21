#!/usr/bin/env python3
"""yield values"""
import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """define func"""
    start = time.time()
    await asyncio.gather(*(async_compreihension() for _ in range(4)))
    end = time.time()
    return end - start
