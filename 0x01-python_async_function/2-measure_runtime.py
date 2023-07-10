#!/usr/bin/env python3
"""
A function that create a measure_time function with integers n and max_delay
as arguments that measures the total execution time
"""


import asyncio
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function that get the current time in seconds before and
    after running the wait_n coroutin.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
