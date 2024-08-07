#!/usr/bin/env python3
"""
Script that defines and runs the wait_n coroutine, which utilizes wait_random.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates and runs n instances coroutine with a given max_delay.

    Args:
        n (int): The number of times to run the wait_random coroutine.
        max_delay (int): The maximum delay time for the wait_random coroutine.

    Returns:
        List[float]: A list of the actual delays experienced.
    """
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)
    return results
