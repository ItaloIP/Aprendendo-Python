from time import sleep


def Maior(*lista):
    print('~~' * len(lista))
    print('Valores:')
    for c in lista:
        print(c, end=' ')
        sleep(0.3)
    print(f' | Há {len(lista)} números.')
    print('-='*10)
    if len(lista) == 0:
        print(f'O maior valor é 0')
    else:
        print(f'O maior valor é {max(lista)}')
    print('-='*10)



#Programa Principal
Maior(3, 5, 8, 1)
Maior(1, 5, 8, 10, 15, 3, 200)
Maior(100, 640, 1245, 15)
Maior(1)
Maior()
