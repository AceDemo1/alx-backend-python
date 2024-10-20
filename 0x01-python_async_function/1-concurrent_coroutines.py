#!/usr/bin/env python3
"""random delay"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
import random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """define func"""
    task = [asyncio.create_task(wait_random(max_delay)) for j in range(n)]
    j = []
    for k in asyncio.as_completed(task):
        l = await k
        j.append(l)
    return j
