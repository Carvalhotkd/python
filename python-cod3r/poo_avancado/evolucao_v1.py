#!/usr/bin/python3
class Humano:
    #atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
    
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'

if __name__ == '__main__':
    jose = Humano('José')
    gronkn = Humano('gronkn')
    gronkn.das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'gronkn.especie {gronkn.especie}')