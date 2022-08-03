num = int(input('Digite um número inteiro: '))
pa = int(input('Digite a razão aritmética: '))
termo = pa
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=' > ')
        termo += pa
        cont += 1
    mais = int(input('Quer mais quantos termos?'))
print('Ao total, foram {} termos.'.format(cont - 1))
