#!/usr/bin/env python3
"""annotate func"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """define func"""
    return [(i, len(i)) for i in lst]
