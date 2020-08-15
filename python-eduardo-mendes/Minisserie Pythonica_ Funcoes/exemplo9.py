"""Funções parciais."""

from operator import add, mul
from functools import partial, reduce

soma_2 = partial(add, 2)
mul_2 = partial(mul, 2)

print(soma_2(0))
print(soma_2(2))

print(reduce(add, [1, 2, 3, 4, 5])) # somatório
print(reduce(mul, [1, 2, 3, 4, 5])) # multiplicação

somatorio = partial(reduce, add)
multiplicatorio = partial(reduce, mul) # sim multiplicatorio o.0
mul_2_all = partial(map,mul_2)

print(somatorio([1, 2, 3, 4]))
print(multiplicatorio([1, 2, 3, 4]))