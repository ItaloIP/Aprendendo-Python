primo = int(input('Digite um número: '))
for c in range(1,99):
    test = primo / c
if test == 0.0:
    print('O número {} não é primo.'.format(primo))
else:
    print('O número {} é primo.'.format(primo))
