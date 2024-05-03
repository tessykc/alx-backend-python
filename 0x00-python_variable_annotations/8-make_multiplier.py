#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the product.
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
