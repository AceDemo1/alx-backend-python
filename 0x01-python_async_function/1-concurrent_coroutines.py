#!/usr/bin/env python3
"""random delay"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """define func"""
    delays = [asyncio.create_task(wait_random(max_delay)) for j in range(n)]
    tasks = []
    for k in asyncio.as_completed(delays):
        task = await k
        j.append(task)
    return tasks
