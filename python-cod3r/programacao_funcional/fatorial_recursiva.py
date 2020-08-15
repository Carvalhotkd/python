#!/usr/bin/python3
def fatorial(n):
    return n * (fatorial(n-1) if (n-1) > 1 else 1)

if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')
    #fatorial de 10 é a mesma quantidade de segundos que tem 6 semanas
    print(6 * 7 * 24 * 60 * 60)