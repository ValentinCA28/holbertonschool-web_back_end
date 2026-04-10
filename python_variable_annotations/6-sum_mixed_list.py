#!/usr/bin/env python3
"""Module that provides a sum_mixed_list function with type annotations."""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Sum a list of integers and floats and return the total as a float."""
    return float(sum(mxd_lst))
