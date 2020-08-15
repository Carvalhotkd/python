"""Anotações de tipo """

# def soma(x: int, y: int) -> int:
#     return x + y

# def soma(x: [int, float, complex], y: [int, float, complex]) -> [int, float, complex]:
#     return x + y

# from numbers import Number

# def soma(x: Number, y: Number) -> Number:
#     return x + y

from numbers import Number
from typing import Union

Somavel = Union[Number, str, list]

def soma(x: Somavel, y: Somavel) -> Somavel:
    return x + y