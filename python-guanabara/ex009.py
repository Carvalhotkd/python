#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
n1 = int(input('Digite um número para ver sua tabuada: '))
print('-'*15)
for n in range(11):
    print(f'{n1} X {n} = {n*n1}')
print('-'*15)