# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triâgulo
# retângulo, calcule e mostre o comprimento da hipotenusa



# sem importação
# catO = float(input('Qual o comprimento do cateto oposto: '))
# catA = float(input('Qual o comprimento do cateto adjacente: '))
# hip = (catO ** 2 + catA ** 2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'. format(hip))

from math import hypot
catO = float(input('Qual o comprimento do cateto oposto: '))
catA = float(input('Qual o comprimento do cateto adjacente: '))
hip = hypot(catO,catA)
print('A hipotenusa vai medir {:.2f}'. format(hip)) 