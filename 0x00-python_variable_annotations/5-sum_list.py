#!/usr/bin/env python3
"""Sum list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of the input list of floats.
    """
    return sum(input_list)
