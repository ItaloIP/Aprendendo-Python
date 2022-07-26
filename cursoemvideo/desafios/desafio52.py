primo = int(input('Digite um número: '))
tot = 0
for c in range(1, primo + 1):
    if primo % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m',end='')
    print('{} '.format(c),end='')

print('O número {} foi divisível {} vezes'.format(primo,tot))
if tot == 2:
    print('Ele é primo!')
else:
    print('Ele não é PRIMO')
