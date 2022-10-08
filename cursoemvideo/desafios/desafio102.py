def Fatorar(number, show=False):
    """
    -> Função para calcular o fatorial de um número.
    :param number: Número que vai ser pego no programa principal.
    :param show: (opcional) Mostrar ou não a conta na tela.
    :return: Valor do Fatorial de um número number.
    """
    print('--'*15)
    f = 1
    for c in range(number, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} x',end=' ')
            else:
                print(' = ', end='')
    return f



#Programa Principal
num = int(input('Fatoração: '))
print(Fatorar(num, True))
