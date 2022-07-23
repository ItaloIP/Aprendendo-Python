print('=-' * 15)
print('\033[0;32;45mAnalisador de Triângulos 2.0\033[m')
print('=-' * 15)

m1 = float(input('Escreva a primeira medida: '))
m2 = float(input('A segunda medida: '))
m3 = float(input('E a última medida: '))

if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    if m1 == m2 == m3:
        print('Estas medidas podem formar um triângulo EQUILÁTERO')
    elif m1 == m2 or m1 == m3 or m2 == m3:
        print('Estas medidas podem formar um triângulo ISÓSCELES')
    else:
        print('Estas medidas podem formar um triângulo ESCALENO')
else:
    print('Estas medidas não podem formar um triângulo.')