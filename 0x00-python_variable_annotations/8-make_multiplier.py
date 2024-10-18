#!/usr/bin/env python3
"""returns a func"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """define func"""
    ret = lambda n: n *multiplier 
    return ret
