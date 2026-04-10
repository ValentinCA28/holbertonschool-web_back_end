#!/usr/bin/env python3
"""Module that provides a sum_list function with type annotations."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum a list of floats and return the total as a float."""
    return sum(input_list)
