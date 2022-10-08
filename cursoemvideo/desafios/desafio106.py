from time import sleep


def helpe(search=''):
    print('\033[0;37;43m~~\033[m'*20)
    print(f'\033[0;37;43mAcessando os documentos do "{search}"\033[m')
    print('\033[0;37;43m~~\033[m'*20)
    sleep(0.6)
    print(f'\033[0;30;47m')
    help(search)
    sleep(4)
    print()



#Programa principal
while True:
    print('\033[0;37;42m~\033[m'*18)
    print(' \033[0;37;42mMe da um HELPE!\033[m')
    print('\033[0;37;42m~\033[m'*18)
    Search = str(input('Função ou Biblioteca > '))
    if Search.lower() == 'fim':
        print('\033[0;30;41m ATÉ LOGO!')
        break
    else:
        helpe(Search)
