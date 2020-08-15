#!/usr/bin/python3

def fibonacci(quantidade):
    resultado = [0,1]
    for _ in range(2, quantidade):
        """nesse caso o contador i foi substituido por (_), por ser
        uma variavel que não sera usada"""
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    #listar os 20 primeiros números da sequencia
    for fib in fibonacci(20):
        print(fib)
    