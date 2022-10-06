from time import sleep


def Contador(ini, fin, pa):
    if pa < 0:
        pa *= -1
    print('-='*20)
    print(f'Contagem de {ini} à {fin} de {pa} em {pa}')
    if fin < ini:
        fin = fin - 1
        if pa > 0:
            pa = -(pa)
    else:
        fin = fin + 1
        if pa < 0:
            pa = -(pa)

    for fin in range(ini, fin, pa):
        print(fin, end=' ')
        sleep(0.3)
    print('fim!')
    print('-='*20)


# Programa Principal
Contador(0,10,1)
Contador(10,0,2)
print('Sua vez de fazer uma progressão aritmética')
a = int(input('Início: '))
b = int(input('Final: '))
while True:
    c = int(input('Passo: '))
    if c != 0:
        break
    else:
        print('O passo não pode ser menor que 0!')
Contador(a, b, c)
