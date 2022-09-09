numbers = list()
while True:
    numbers.append(int(input('Digite qualquer número: ')))

    choice = str(input('Quer continuar ?[S/N]:  ')).strip().upper()
    if choice == 'N':
        break
    
print('-='*20)
numbers.sort(reverse=True)
print(f'Você digitou {len(numbers)}')
print(numbers)
if 5 in numbers:
    print('O número 5 está na lista!')
else:
    print('O número 5 não se encontra na lista!')
