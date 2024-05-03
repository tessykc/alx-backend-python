#!/usr/bin/env python3

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a list.

    Args:
        lst (Sequence[Any]): The input list.

    Returns:
        Union[Any, None]: The first element of the list if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
