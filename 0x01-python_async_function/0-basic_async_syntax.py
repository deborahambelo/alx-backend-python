#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that takes in an integer argument (max_delay)
and waits for a random delay between 0 and max_delay seconds before returning the delay.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns the delay.

    Args:
        max_delay (int): The maximum delay time in seconds. Default is 10 seconds.

    Returns:
        float: The random delay time.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
