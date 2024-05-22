#!/usr/bin/env python3
"""Type checking"""

from typing import Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in on the elements of a tuple by repeating them 'factor' times.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int, optional): The zoom factor (default is 2).

    Returns:
        Tuple[int, ...]: The zoomed-in tuple.
    """
    zoomed_in = tuple(item for item in lst for _ in range(factor))
    return zoomed_in


array = (12, 72, 91)  # Use parentheses to create a tuple

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
