#!/usr/bin/env python3
"""
Module to measure the average execution time of the wait_n coroutine.
"""

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time per call of the wait_n coroutine.

    Args:
        n (int): The number of times to run the wait_n coroutine.
        max_delay (int): The maximum delay time for each coroutine.

    Returns:
        float: The average time taken to execute wait_n per call in seconds.
    """
    start_time = time.time()

    await wait_n(n, max_delay)

    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
