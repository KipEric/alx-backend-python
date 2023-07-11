#!/usr/bin/env python3
"""
This is a module that calculate the time used
to execute async_comprehension

"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A function that calculate run_time
    """
    start = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
