s = 0
for c in range(0,6):
    n1 = int(input('Digite um valor inteiro: '))
    re = n1 % 2
    if re == 0:
        s += n1
print('O resultado entre todos os números PARES é de {}')
