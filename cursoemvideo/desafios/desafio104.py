def Éint(num):
    while True:
        num = str(input(num))
        if num.isnumeric() == False:
            print('\033[0;31;40m ISSO NÃO É NÚMERO!!! DIGITE UM NÚMERO REAL!\033[m')
        else:
            break


#Programa Principal
n = Éint('Digite qualquer número: ')
print(f'\033[0;32;40m Número reconhecido!\033[m')
