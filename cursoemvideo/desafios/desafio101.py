def Votar(idade):
    """
    -> Função para calcular a idade e ver se vai votar.
    :param idade: Pegar o valor da variável 'ano' da lin30
    :return: retorna um respectivo item referente a idade
    """
    from datetime import date
    s = date.today().year - ano
    print(f'Com {s} anos: ', end='')
    if s <= 15:
        return 'Não vota!'
    elif 16 <= s < 18 or s > 65:
        return 'Voto Opcional!'
    else:
        return 'Voto OBRIGATÓRIO!'


#Programa Principal
ano = int(input('Ano de nascimento: '))
print(Votar(ano))
