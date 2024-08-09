#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather
    """
    begin = time.time()
    tasks = [
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            ]
    await asyncio.gather(*tasks)
    elapsed = time.time() - begin
    return elapsed
