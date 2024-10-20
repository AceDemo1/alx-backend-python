#!/usr/bin/env python3
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio, random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """define func"""
    i = [asyncio.create_task(wait_random(max_delay)) for j in range(n)]
    j = [] 
    for k in asyncio.as_completed(i):
        l = await k
        j.append(l)
    return j
