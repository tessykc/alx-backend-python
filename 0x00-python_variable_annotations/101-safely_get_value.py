#!/usr/bin/env python3
"""Safely get value"""

from typing import TypeVar, Mapping, Any, Union

# Define a type variable for the default value
T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value to
        return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key, or the
        default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
