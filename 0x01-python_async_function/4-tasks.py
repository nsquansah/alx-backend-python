#!/usr/bin/env python3
"""Defines a function `task_wait_n` for Task_4"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """An identical functin to `wait_n` from the `3-tasks` module"""
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = [await task for task in asyncio.as_completed(tasks)]

    return delays
