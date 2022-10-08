def Ficha(name='<desconhecido>', gols = '0'):
    """
    -> Cadastro de jogadores 
    :param name: (opcional) Recebe o nome do programa principal (caso não haja valor, será retornado = <desconhecido>)
    :param gols: (opcional) Recebe o valor do gol em STR e depois se transforma em INT SE for um número REAL! Se não, será retornado = 0
    """
    if name == '':
        name = '<desconhecido>'
    else:
        name = name
            
    if gols.isnumeric():
        gols = int(gols)
    else: 
        gols = 0

    return f'O {name} fez {gols} gols.'



#Programa Principal
nome = str(input('Nome do jogador: ')).strip().capitalize()
gol = str(input(f'Quantos gols o {nome} fez?: ')) 
print(Ficha(nome, gol))
