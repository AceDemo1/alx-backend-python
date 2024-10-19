#!/usr/bin/env python3
"""annotate func"""
from typing import Union, Mapping, Any, TypeVar


ty = TypeVar('ty')
def safely_get_value(dct: Mapping[Any, ty], key: Any, default: Union[ty, None] = None) -> Union[ty, None]:
    """define func"""
    if key in dct:
        return dct[key]
    else:
        return default
