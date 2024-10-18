#!/usr/bin/env python3
"""takes list and return their sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """define func"""
    j = 0
    for i in mxd_list:
        j += i
    return j
