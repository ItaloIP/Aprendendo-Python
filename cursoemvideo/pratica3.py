def pi(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if pi(num, True):
    print('Par')
else:
    print('Não é par')
