#!/usr/bin/env python3
"""
A function task_wait_random that takes an integer
max_delay and returns a asyncio.Task.
"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    rout = wait_random(max_delay)
    task = asyncio.create_task(rout)
    return task
