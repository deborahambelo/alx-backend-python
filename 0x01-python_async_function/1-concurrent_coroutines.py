#!/usr/bin/env python3
"""
Script that defines and runs the wait_n coroutine, which utilizes wait_random.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    runs n instances of the wait_random coroutine.

    Args:
        n(int): The number of times to run the wait_random coroutine.
        max_delay(int): The maximum delay time.

    Returns:
        List[float]: A list of the actual delays experienced.
    """
    delays = []

    async def append_delay():
        delay = await wait_random(max_delay)
        delays.append(delay)
        return delay

    await asyncio.gather(*(append_delay() for _ in range(n)))
    return sorted(delays)
