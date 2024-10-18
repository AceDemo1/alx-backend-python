#!/usr/bin/env python3
"""returns tuple"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v ** 2)
