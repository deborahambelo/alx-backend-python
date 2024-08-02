#!/usr/bin/env python3
'''
Given the parameters and return values, add type annotations to the function
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
'''


from typing import Mapping, Any, Union, Sequence, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None]) -> Union[Any, T]:
    '''
    Code anotated
    '''
    if key in dct:
        return dct[key]
    else:
        return default
