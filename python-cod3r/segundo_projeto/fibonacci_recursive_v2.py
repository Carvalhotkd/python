#!/usr/bin/python3
def fibonacci(quantidade, sequencia=(0,1)):
    """implementa a formula fibonacci."""
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == '__main__':
    for fib in fibonacci(20):
        """lista os 20 primeiros números da sequencia."""
        print(fib)