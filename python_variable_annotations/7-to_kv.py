#!/usr/bin/env python3
"""Module that provides a to_kv function with type annotations."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a key-value pair returning tuple with squared value as float."""
    return (k, float(v ** 2))
