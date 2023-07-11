#!/usr/bin/env python3
"""Defines function `task_wait_random` for Task_3"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an `asyncio.Task` object representing a Task object"""
    task_random: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task_random
