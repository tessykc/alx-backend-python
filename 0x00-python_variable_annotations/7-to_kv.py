#!/usr/bin/env python3

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string `k` and an `int` or `float` `v` and returns a tuple.
    The first element of the tuple is `k`, and the second element is the square of `v`.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple containing `k` and the square of `v`.
    """
    return k, v ** 2