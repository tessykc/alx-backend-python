#!/usr/bin/env python3


from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Accepts a mixed list of integers and floats and returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
        float: The sum of the integers and floats in the input list.
    """
    return sum(mxd_lst)
