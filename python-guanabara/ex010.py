#Crie um programa que leia quanto dinheito uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar
#considere US$1.00 = R$3.27 (saudades)
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = 3.27
print(f'Com R${real} você pode comprar US${real/dolar:.2f}')