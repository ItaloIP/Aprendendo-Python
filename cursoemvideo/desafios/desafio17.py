#Calcular a hipotenusa
from math import hypot
co = float(input('Informe o comprimento do Cateto Oposto: '))
ca = float(input('Informe o comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)
print('O cálculo da hipotenusa é {:.2f}.'.format(hi))
