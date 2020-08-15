"""Funções de ordem superior HOFs."""
from typing import Callable, Any

soma_2 = lambda val: val + 2


#Twice
def reaplica(func: Callable, val: Any) -> Any:
    """Função que reaplica a função ao resultado da chamada."""
    return func(func(val))

print('sem usar a função reaplica')
print(soma_2(0))
print(soma_2(2))
print('reaplicando função manualmente')
print(soma_2(soma_2(0)))
print(soma_2(soma_2(2)))
print('Utilizando a função reaplica')
print(reaplica(soma_2, 0))
print(reaplica(soma_2, 2))