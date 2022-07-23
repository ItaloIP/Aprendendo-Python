n1 = float(input('Digite a sua primeira Nota: '))
n2 = float(input('Digite a sua segunda Nota: '))
m = (n1 + n2) / 2

print('A sua média foi {:.2f}'.format(m))

if m < 5.00:
    print('Você está REPROVADO!')

elif m >= 5.00 and 6.99:
    print('Você está em RECUPERAÇÃO!')

elif m >= 7.00:
    print('Você passou!')
