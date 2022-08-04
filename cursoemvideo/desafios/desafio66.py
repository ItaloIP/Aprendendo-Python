cont = sm = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    cont += 1
    sm += n
print(f'A soma entre os {cont} valores é {sm}')
