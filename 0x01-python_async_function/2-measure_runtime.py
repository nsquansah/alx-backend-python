#!/usr/bin/env python3
"""Defines an async function, `measure_time` for Task_2"""
import asyncio
from typing import List

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for `wait_n(n, max_delay`
    Args:
        n (int): first argument of the `wait_n` function
        max_delay (int): second argument for the `wait_n` function
    Returns:
        the quotient of total_time / n
    """
    import time
    total_time: float = 0.0

    start_time: float = time.perf_counter()
    delays: List[float] = asyncio.run(wait_n(n, max_delay))
    end_time: float = time.perf_counter()
    for delay in delays:
        total_time += delay

    return total_time / n
