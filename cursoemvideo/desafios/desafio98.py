from time import sleep
def Contador(ini, fin, pa):
    for b in range(ini, fin, pa):
        print(b, end=' ')
        sleep(0.6)


# Programa Principal
# print('Contagem de 0 à 10 de 1 em 1')
# for c in range(0, 11):
#     print(c, end=' ')
#     sleep(0.3)
# print() # linha vazia
# print('-='*20)
# print('Contagem de 10 a 0 de 2 em 2')
# for v in range(10, -1, -2):
#     print(v, end=' ')
#     sleep(0.3)
# print() # linha vazia
# print('-='*20)
# print('Sua vez de fazer uma progressão aritmética')

a = 0
b = 0

a = int(input('Início: '))
b = int(input('Final: '))
while True:
    c = int(input('Passo: '))
    if c != 0:
        break
    else:
        print('O passo não pode ser menor que 0!')
if b < a:
    c = -(c)
else:
    b =+ 1

Contador(a, b, c)
