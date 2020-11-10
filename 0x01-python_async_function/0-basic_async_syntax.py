#!/usr/bin/env python3

import random
import asyncio


""" Async """


async def wait_random(max_delay=10):

    """
    synchronous coroutine that takes
    in an integer argument

    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
