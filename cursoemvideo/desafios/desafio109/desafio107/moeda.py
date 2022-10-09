def met(number, format=False):
    res = number / 2
    return res if format == False else moeda(res)


def dob(number = 0.0, format=False):
    res = number * 2
    return res if format == False else moeda(res)


def aumentar(number = 0.0, taxa = 0.0, format=False):
    res = number + (number * taxa / 100)
    return res if format == False else moeda(res)


def diminuir(number=0.0, taxa=0, format=False):
    res = number - (number * taxa / 100)
    return res if format == False else moeda(res)


def moeda(preço = 0.0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')
