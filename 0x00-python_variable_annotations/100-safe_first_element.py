#!/usr/bin/env python3
""" Module for type hint """
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Duck typing - first element of a sequence """
    if lst:
        return lst[0]
    else:
        return None
