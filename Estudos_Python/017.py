"""
co = float(input('Comprimento do cateto oposto'))
ca = float(input('Comprimento do cateto adjacente'))
h = (co ** 2 +_ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))
essa é uma das maneiras tradicionais de calcular a hipotenusa
"""
import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.hypot (co, ca)
print('A hipotenusa é igual a {:.2f}'.format(h))