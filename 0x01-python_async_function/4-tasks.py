#!/usr/bin/env python3
"""random delay"""
import asyncio
from typing import List
wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """define func"""
    delays = [wait_random(max_delay) for j in range(n)]
    tasks = []
    for k in asyncio.as_completed(delays):
        task = await k
        tasks.append(task)
    return tasks
