#!/usr/bin/env python3
"""Module that provides a task_wait_n coroutine for
concurrent task execution.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute task_wait_random n times and return delays in
    ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for completion in asyncio.as_completed(tasks):
        result = await completion
        results.append(result)
    return results
