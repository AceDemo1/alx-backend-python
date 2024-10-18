#!/usr/bin/env python3
"""takes list and return their sum as a float"""


def sum_list(input_list: list[float]) -> float:
    """define func"""
    j = 0
    for i in input_list:
        j += i
    return j
