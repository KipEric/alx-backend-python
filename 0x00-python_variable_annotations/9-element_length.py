#!/usr/bin/env python3
"""
How to annotate functions parameters and
return values with the appropriate types
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    elements' length
    """
    return[(i, len(i)) for i in lst]
