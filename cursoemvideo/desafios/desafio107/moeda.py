def met(number):
    res = number / 2
    return res


def dob(number):
    res = number * 2
    return res


def aumentar(number, taxa):
    res = number + (number * taxa / 100)
    return res


def diminuir(number=0, taxa=0):
    res = number - (number * 110 / 100)
    return res