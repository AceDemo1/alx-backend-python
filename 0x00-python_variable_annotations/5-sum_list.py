#!/usr/bin/env python3
"""takes list and return their sum as a float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """define func"""
    j = 0
    for i in input_list:
        j += i
    return j
