#!/usr/bin/env python3
"""
A function that is used to check if the task is asyncio
"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    rout = wait_random(max_delay)
    task = asyncio.create_task(rout)
    return task
