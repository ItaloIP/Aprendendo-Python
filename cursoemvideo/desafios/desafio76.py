print('-'*32)
print(f'{"Lista de Preços":^30}')
print('-'*32)

tupla = ('GTX 1650', 1500,
        'RTX 2060', 2500,
        'RTX 2080', 3000,
        'Headset Gamer', 350,
        'Pc Gamer', 5999.99,

        )
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<23}', end='')
    else:
        print(f'R${tupla[pos]:>5.2f}')
print(('-'*32))
