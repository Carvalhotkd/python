#!/usr/bin/python3
from random import randint

numero_informado = -1
numero_secreto = randint(0,9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o número: '))

print(f'O número secreto {numero_secreto} foi encontrado!')