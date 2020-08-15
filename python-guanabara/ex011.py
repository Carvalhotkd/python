#Faça umprograma que leia a largura e a altura de uma parede em metros,
#calcule sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
print(f'Sua parede tem a dimensão de {altura}x{largura} e sua área é de {largura*altura}m².')
print(f'Para pintar essa parede, você precisará de {(largura*altura)/2}l de tinta.')