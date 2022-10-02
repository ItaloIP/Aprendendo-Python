jogadores = list()
jogador = dict()
gol = []

# ----- #
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))

    for c in range(0, partidas): #Pega os dados de partidas e faz um laço daquele valor
        gol.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {c + 1}? ')))

    jogador['gols'] = gol[:] #Copia o que foi adicionado em 'gol'
    jogador['total'] = sum(gol)

    choice = str(input('Quer continuar? [S/N]:  ')).strip().upper()[0]
    jogadores.append(jogador.copy())
    if choice == 'N':
        break
    else:
        jogador.clear()



print('-='*30)
print('COD NOME    | GOLS       | TOTAL')
for c, v in enumerate(jogadores):
    print(f' {c}  {v["nome"]}      {v["gols"]}      {v["total"]}')
print('-='*30)
while True:
    choice = int(input('Mostrar dados de qual jogador? [COD 999 para finalizar]: '))
    if choice == 999:
        break
    if choice >= len(jogadores):
        print(f'ERRO!! não existe jogador com o código {choice}')
    else:
        print(f' Análise do jogador {jogadores[choice] ["nome"]}')
        for i, g in enumerate(jogadores[choice]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
print('-='*20)
