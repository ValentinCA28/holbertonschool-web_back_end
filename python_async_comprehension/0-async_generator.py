#!/usr/bin/python3
"""Module that provides an async_generator coroutine."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """Generate 10 random numbers between 0 and 10 with 1 second delay each."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
