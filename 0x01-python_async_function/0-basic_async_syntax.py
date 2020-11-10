#!/usr/bin/env python3

import random


""" Async """


def wait_random(max_delay=10):

    """
    synchronous coroutine that takes
    in an integer argument

    """
    yield
    return random.uniform(0, max_delay)
