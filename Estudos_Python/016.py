import math
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua versão inteira é {}'.format(num, math.trunc(num)))

"""a função math.trunc quebra o número, deixando ele por inteiro, porém da para 
fazer tambem usando 'int' na variavel para usar o inteiro, sem precisar importar math"""