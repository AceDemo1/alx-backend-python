#!/usr/bin/env python3
"""yield values"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprhension() -> List[float]:
    """define func"""
    collections = [i async for i in async_generator()]
    return collections
