def ReadInt(num1):
    while True:
        try:
            num1 = int(input(num1))
        except (ValueError, TypeError):
            print('\033[0;31;40mERROR: Digite um valor um número da clase inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31;40mUsuário encerrou o programa.\033[m')
            return 0
            
        else:
            return num1

def ReadFloat(num2 = 0):
    while True:
        try:
            num2 = float(input(num2))
        except ValueError:
            print('\033[0;31;40mERROR: Digite um valor um número da clase inteiro!\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31;40mUsuário encerrou o programa.\033[m')
            return 0
        else:
            return num2


