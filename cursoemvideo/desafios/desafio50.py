s = 0
cont = 0
for c in range(0,6):
    n1 = int(input('Digite o {} valor inteiro: '.format(c)))
    if n1 % 2 == 0:
        s += n1
        cont += 1
print('Você informou {} números pares, resultado entre todos os números PARES é de {}'.format(cont,s))
