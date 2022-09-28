from random import randint
from time import sleep
from operator import itemgetter

dados = {
    'Jogador_1': randint(1, 6),
    'Jogador_2': randint(1, 6),
    'Jogador_3': randint(1, 6),
    'Jogador_4': randint(1, 6),
}


# ------------- #
placar = dict()
print('Valores sorteados:')

for k, v in dados.items():
    print(f'{k} tirou {v}.')
    sleep(1)

print('-='*20)
print('    -= PLACAR DE LÍDERES =-')
print('-='*20)
placar = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(placar):
    print(f'    {i+1}° Lugar: {v[0]} com {v[1]}')
    sleep(1)
