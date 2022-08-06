from random import randint
from time import sleep
itens = 'PEDRA', 'PAPEL', 'TESOURA'

print('Jokenpô!')

robo = int(randint(0,2))
escolha = int(input(''' Escolha : 
( 0 ) PEDRA
( 1 ) PAPEL
( 2 ) TESOURA
: '''))

print('-='*8)
print('Você JOGOU {}'.format(itens[escolha]))
print('O ROBO jogou {}.'.format(itens[robo]))
print('-='*8)

sleep(0.9)

if robo == 0: #ROBO joga PEDRA
    if escolha == 0: #JOGADOR joga PEDRA
        print('EMPATE')
    elif escolha == 1: #JOGADOR joga PAPEL
        print('você GANHOU')
    elif escolha == 2: #JOGADOR joga TESOURA
        print('ROBO GANHOU')
    else: #JOGADOR escolheu algo INVÁLIDO
        print('JOGADA INVÁLIDA!')

elif robo == 1: #ROBO joga PAPEL
    if escolha == 0: #JOGADOR joga PEDRA
        print('você GANHOU!')
    elif escolha == 1: #JOGADOR joga PAPEL
        print('EMPATE!')
    elif escolha == 2: #JOGADOR joga TESOURA
        print('VOCÊ GANHOU!')
    else: #JOGADOR escolheu algo INVÁLIDO
        print('Jogada inválida')

elif robo == 2: #ROBO joga TESOURA
    if escolha == 0: #JOGADOR joga PEDRA
        print('você GANHOU!')
    elif escolha == 1: #JOGADOR joga PAPEL
        print('ROBO GANHOU!')
    elif escolha == 2: #JOGADOR joga TESOURA
        print('EMPATE!')
    else: #JOGADOR escolhe algo INVÁLIDO
        print('JOGADA INVÁLIDA!')
