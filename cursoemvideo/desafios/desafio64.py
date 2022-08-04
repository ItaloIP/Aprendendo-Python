s = -999
cont = c = 0
n = int(input('Digite um número (digite "999" para parar): '))
s += n
while n != 999:
    n = int(input('Digite um número (digite "999" para parar): '))
    cont += 1
    s += n
print('Você digitou {} números e ao todo a soma deles foram de {}.'.format(cont,s))
