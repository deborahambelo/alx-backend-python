#!/usr/bin/env python3
'''
type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    takes a float
    returns a function that takes a float and returns a float
    '''
    def mult(n: float) -> float:
        '''
        multiplies float n by multiplier from above
        '''
        return n * multiplier
    return mult
