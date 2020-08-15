#Escreva um programa que leia um valor em metros e exiba seu valor convertido em centimetros e milimetros
n = float(input('Uma distância em metros: '))
print(f'A medida de {n}m corresponde a:')
print(f'{n/1000}km')
print(f'{n/100}hm')
print(f'{n/10}dam')
print(f'{n*10}dm')
print(f'{n*100}cm')
print(f'{n*1000}mm')