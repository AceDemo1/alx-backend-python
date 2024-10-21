#!/usr/bin/env python3
"""random delay"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """define func"""
    start = time.time()
    task = asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
