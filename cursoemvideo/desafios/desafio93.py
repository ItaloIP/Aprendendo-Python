jogador = dict()
gol = []
total = 0

# ----- #

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))

for c in range(0, partidas): #Pega os dados de partidas e faz um laço daquele valor
    gol.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {c + 1}? ')))

jogador['gols'] = gol[:] #Copia o que foi adicionado em 'gol'


jogador['total'] = sum(gol)

print('-='*30)
print(jogador)
print('-='*30)

for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}')
print('-='*30)

print(f'O jogador, {jogador["nome"]}, jogou {partidas} partidas.')
for c, v in enumerate(gol):
    print(f'    ¬ Na partida {c}, fez {v}')
print(f'Total de {jogador["total"]} gols.')
