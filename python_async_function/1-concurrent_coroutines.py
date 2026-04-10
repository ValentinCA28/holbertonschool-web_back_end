#!/usr/bin/env python3
"""Module that provides a wait_n coroutine for concurrent execution."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random n times concurrently and return delays in ascending
    order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []
    for completion in asyncio.as_completed(tasks):
        result = await completion
        results.append(result)
    return results
