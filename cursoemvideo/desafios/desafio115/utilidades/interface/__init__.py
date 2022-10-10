def Opc(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERROR!! Digite um valor válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário parou de executar o programa.\033[m')
        else:
            return n


def lin(tam=42):
    return '-' * tam


def tit(txt):
    print(lin())
    print(txt.center(42))
    print(lin())


def menu(lista):
    tit('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(lin())
    opc = Opc('\033[32mOpção:  \033[m')
    return opc
