"""Des | empacotamento de argumentos."""
# def my_sum(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
#     return sum((a,b,c,d,e,f,g,h,i,j,k,l,m,n,o))

# def my_sum(*args):
#     print(args)
#     print(type(args))
#     return sum(args)

def my_sum(*grupo_posicional, **grupo_nomeado):
    print(f'Grupo posicional: {grupo_posicional}')
    print(f'Grupo nomeado: {grupo_nomeado}')
    print(f'Tipo grupo posicional: {type(grupo_posicional)}')
    print(f'Tipo grupo nomeado: {type(grupo_nomeado)}')
    return grupo_posicional, grupo_nomeado

lista = [-1, 2, 3, 4, 5]

def my_min(*args):
    return min(*args)

dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

def my_max(a = 0, b = 0, c = 0, d = 0):
    return max((a, b, c, d))

print(my_max(**dicionario))

l = [1, 2, 3]
d = {
    'd': 4, 
    'e': 5
    }

def my_mix(a, b, c, d=0, e=0):
    return a, b, c, d, e

print(my_mix(*l))
print(my_mix(*l, **d))