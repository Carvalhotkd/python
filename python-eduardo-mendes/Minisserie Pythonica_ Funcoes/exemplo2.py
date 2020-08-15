"""Série de funções 2 """

anonima = lambda param: param + 2
anonima_plus = lambda param1, param2: param1 + param2

def soma_posicional(x, y):
    return x + y

def soma_nomeados(x=7, y=7):
    """ 
        na falta de valor x e y o valor 7 será usado
    """
    return x + y

def soma_explicitamente_nomeados(*, x=7, y=7):
    """ 
        por causa do * ao enviar um parametro tem que expecificar se é x ou y
    """
    return x + y

def soma_explicitamente_nomeados2( x=7,*, y=7):
    """ 
        somente o y deve ser especificado
    """
    return x + y