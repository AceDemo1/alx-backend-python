#!/usr/bin/env python3
from typing import Sequence, Any, Union
"""annotate func"""
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """define func"""
    if lst:
        return lst[0]
    else:
        return None
