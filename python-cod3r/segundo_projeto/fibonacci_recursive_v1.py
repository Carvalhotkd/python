#!/usr/bin/python3
def fibonacci(quantidade, sequencia=(0,1)):
    """implementa a formula fibonacci."""
    if len(sequencia) == quantidade:
        """condição de parada."""
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == '__main__':
    for fib in fibonacci(20):
        """lista os 20 primeiros números da sequencia."""
        print(fib)