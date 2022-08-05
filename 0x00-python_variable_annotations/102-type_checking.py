#!/usr/bin/env python3
'''
Use mypy to validate the following code and apply any necessary changes
def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
'''


from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    Code validated
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array: Tuple[Any, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
