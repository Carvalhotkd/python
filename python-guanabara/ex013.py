#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
sal = float(input('Qual é o salário do funcionario? '))
print(f'Um funcionário que ganhava R${sal}, com 15% de aumento, passa a receber R${sal + (sal*15)/100:.2f}')