def met(number):
    res = number / 2
    return res


def dob(number = 0.0):
    res = number * 2
    return res


def aumentar(number = 0.0, taxa = 0.0):
    res = number + (number * taxa / 100)
    return res


def diminuir(number=0.0, taxa=0.0):
    res = number - (number * taxa / 100)
    return res


def moeda(preço = 0.0, moeda = 'R$'):
    return f' {moeda}{preço:.2f}'.replace('.',',')
