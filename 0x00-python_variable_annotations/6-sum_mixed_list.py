#!/usr/bin/env python3
""" Mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    function sum_mixed_list which takes a list mxd_lst of
    floats and integers and returns their sum as a float.
    """
    return sum(mxd_lst)
