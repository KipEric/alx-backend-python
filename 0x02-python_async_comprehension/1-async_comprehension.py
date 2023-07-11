#!/usr/bin/env python3
"""
Coroutine that collects the random numbers generated in task 0
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async comprehension to loop over generated numbes
    """
    result = [i async for i in async_generator()]
    return result
