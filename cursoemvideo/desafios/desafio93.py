jogador = dict()


# ----- #

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))

for c in range(0, partidas):
    gol = int(input(f'Quantos gols {jogador["nome"]} fez na partida {c}? '))
    jogador['gols'] = gol[:]
    

print(jogador)