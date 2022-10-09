def met(number, format=False):
    res = number / 2
    return res if format == False else moeda(res)


def dob(number = 0.0, format=False):
    res = number * 2
    return res if format == False else moeda(res)


def aumentar(number = 0.0, taxa = 0):
    res1 = number + (number * taxa / 100)
    return res1 


def diminuir(number=0.0, taxa=0):
    res2 = number - (number * taxa / 100)
    return res2 


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço = 0.0, taxaa = 0, taxab = 0.0):
    print('-'*20)
    print(f'{"    Nota Fiscal"} ')
    print('-'*20)
    print(f'Preço: {moeda(preço)}') # type: ignore
    print(f'Dobro do preço:{moeda(dob(preço))}')  # type: ignore
    print(f'Metade do preço:{moeda(met(preço))}')  # type: ignore
    print(f'{taxaa}% de aumento:{moeda(aumentar(preço, taxaa))}')  
    print(f'{taxab}% de desconto:{moeda(diminuir(preço, taxab))}') # type: ignore
    print('-'*20)
