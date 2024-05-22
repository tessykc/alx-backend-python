#!/usr/bin/env python3
""" Element Length"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in the input list and returns
    a list of tuples.
    Each tuple contains an element from the input list and its
    corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable containing elements of type
        Sequence (e.g., list, tuple, string).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains an element and its length.
    """
    return [(i, len(i)) for i in lst]
