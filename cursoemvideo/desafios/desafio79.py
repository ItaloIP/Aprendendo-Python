number = ''
numbers = list()
numbers.append(int(input('Digite qualquer número: ')))

while True:
    choice = str(input('Quer continuar?[S/N]:  ')).strip().upper()
    if choice == 'N':
        break

    #
    elif choice == 'S':
        number = (int(input('Digite outro número: ')))
        if number in numbers:
            print('Número repetido! Não será acrescentado a lista!')
            print('-='*20)
        else:
            numbers.append(number)
            print('Número adicionado.')
            print('-='*20)
print('-='*20)
numbers.sort()
print(f'Você digitou os valores {numbers}')
