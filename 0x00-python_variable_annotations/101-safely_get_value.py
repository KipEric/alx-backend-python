#!/usr/bin/env python3
"""
A function that takes three arguments dct of type Mapping, key and default.
"""


from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    A function that can return an element of any type
    """
    if key in dct:
        return dct[key]
    else:
        return default
