from time import sleep
from math import sqrt

print('\033[0;31;32m-=\033[m'*10)
print('Função Quadrática')
print('\033[0;31;32m-=\033[m'*10)


while True:
    #coleta de dados
    a = int(input('Valor do A: '))
    while True: #caso o usuário coloque 0 no A, o programa vai repetir a pergunta até ele colocar certo
        if a == 0:
            a = int(input('Não existe função quadrática com o A sendo 0. Tente novamente: '))
        else:
            break

    b = int(input('Valor do B (caso não tenha, adiciona "0"): '))
    c = int(input('Valor do C (caso não tenha, adiciona "0"): '))
#calcula o delta da função 
    delta = (b**2) - (4 * a * c) 
    print('-='*10)
    sleep(0.8)


    if a > 0:
        print('A parábola vai ser pra cima (com as duas perninhas pra cima)')
    elif a < 0:
        print('A parábola vai ser pra baixo (com as duas perninhas pra baixo)')
    print('_'*10)


    if delta > 0:
        print('Vão haver duas raízes diferentes.')
    elif delta == 0:
        print('Vão haver duas raízes idênticas.')
    else: 
        print('Não vão haver raízes.')
        break #caso não haja raízes, o programa STOP para evitar problemas!

    print('-='*10)

    print('\033[0;31;30mRaízes\033[m')
    x1 = (-(b) + sqrt(delta)) / (2 * a)
    x2 = (-(b) - sqrt(delta)) / (2 * a)

    print(f'''X1 = {x1}
X2 = {x2}''')

    print('-='*10)

#cálcula as vértices da função quadrática
    print('\033[0;31;30mVértices\033[m')
    xv = (-(b)) / (2*a)
    yv = (-(delta)) / (4*a)
    if a > 0:
        print(f'''O valor da vértice vai ser mínimo
XV: {xv}
YV: {yv}''')
    else:
        print(f'''O valor da vértice vai ser máximo.
XV: {xv}
YV: {yv}''')
    print('-='*20)
    
    #Pergunta pro usuário se quer continuar a usar o programa
    choice = str(input('Quer continuar?: [S/N]: ')).strip().upper()
    if choice == 'S':
        print('Carregando...')
    elif choice == 'N':
        print('Programa encerrando...')
        break

    while choice != 'S' or 'N':
        choice = str(input('Tente novamente! Quer continuar?[S/N]: ')).strip().upper()
        if choice == 'S':
            print('Carregando...')
        elif choice == 'N':
            print('Programa encerrando...')
            break
