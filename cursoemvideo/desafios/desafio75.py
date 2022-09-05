tupla = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite o último número: ',)))

print('-'*20)
print(f'Você digitou os valores {tupla}')
print(f'O número NOVE apareceu {tupla.count(9)} vezes!')

if 3 in tupla:
    print('O número TRÊS está na posição', tupla.index(3)+1)
else:
    print('O valor TRÊS não foi encontrado')

print('Os números pares são', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
