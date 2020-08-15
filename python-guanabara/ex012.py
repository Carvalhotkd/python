#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
produto = float(input('Qual é o preço do produto?'))
print(f'O produto que custava R${produto}, na promoção com desconto de 5% vai custar R${produto - (produto*5)/100:.2f}')