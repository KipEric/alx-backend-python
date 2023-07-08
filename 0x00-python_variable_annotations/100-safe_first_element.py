#!/usr/bin/env python3
"""
Agumenting code to get correct duck_typed annotation
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    function that accept any sequence containing elements of any type
    """
    if lst:
        return lst[0]
    else:
        return None
