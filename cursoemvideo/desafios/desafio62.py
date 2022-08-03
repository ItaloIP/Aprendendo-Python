num = int(input('Digite um número inteiro: '))
pa = int(input('Digite a razão aritmética: '))
cont = 1
co = 0
while cont <= 10:
    num = num + pa
    cont += 1
    co += 1
    print(num, end=' > ')
print('Pausa')

c = int(input('Quantos termos você quer mostrar a mais?: '))
if c != 0:
    while c != 0:
        while cont <= 10 + c:
            num = num + pa
            cont +=1
            co += 1
            print(num, end=' > ')
