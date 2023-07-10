#!/usr/bin/env python3
"""
A function that create tasks that run wait random concurrently
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that returns an iterator that yields the tasks as finished
    """
    tasks = []
    delays = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
