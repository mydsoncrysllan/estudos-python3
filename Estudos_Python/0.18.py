import math
angulo = float(input('Digite o angulo que você deseja:'))
seno = math.sin(math.radians(angulo))
print('O angulo de {} é igual a {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} é igual a {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} é igual a {:.2f}'.format(angulo, tangente))