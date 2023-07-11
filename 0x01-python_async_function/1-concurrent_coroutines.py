#!/usr/bin/env python3
"""Defines an async function for Task 1 module"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls `wait_random` function @n time with max_delay
    Args:
        n (int): The number of times to call `wait_random` function
        max_delay (int): The maximum limit of delay in seconds
    Returns: A list of all delays
    """
    tasks: List[asyncio.Task] = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
