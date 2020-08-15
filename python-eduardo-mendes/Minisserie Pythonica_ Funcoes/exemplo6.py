"""Funções como objeto de primeira classe."""

from typing import Callable, Dict
from numbers import Number

func = lambda: 'resultado da função'

calc: Dict[str, Callable] = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,
}

print(calc['soma'](5,7))
print(calc['sub'](5,7))
print(calc['mult'](5,7))
print(calc['div'](5,7))

def soma(x: Number, y: Number) -> Number:
    """Soma dois números."""
    return x + y

def sub(x: Number, y: Number) -> Number:
    """Subtrai dois números."""
    return x - y

def mult(x: Number, y: Number) -> Number:
    """Multiplica dois números."""
    return x * y

def div(x: Number, y: Number) -> Number:
    """Divide dois números."""
    return x / y

calc_nomeado = {
    'soma': soma,
    'sub': sub,
    'mult': mult,
    'div': div,
}

print(calc_nomeado['soma'](3,4))
print(calc_nomeado['sub'](3,4))
print(calc_nomeado['mult'](3,4))
print(calc_nomeado['div'](3,4))