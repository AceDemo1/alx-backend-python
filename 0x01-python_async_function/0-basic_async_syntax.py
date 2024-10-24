#!/usr/bin/env python3
"""random delay"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """define func"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
