from poo_01_abstracao_de_dados import Fila


supermercado = Fila()
supermercado.entrar('Felipe')
supermercado.entrar('Fernando')
supermercado.entrar('Luiz')

print(supermercado.fila)
supermercado.sair()
print(supermercado.fila)
supermercado.sair()
print(supermercado.fila)
supermercado.sair()
print(supermercado.fila)