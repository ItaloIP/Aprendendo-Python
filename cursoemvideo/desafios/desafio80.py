#não pode usar sort()
numbers = list()
for c in range (0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > numbers[-1]:
        numbers.append(n)
        print('Valor adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(numbers):
            if n <= numbers[pos]:
                numbers.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados foram: {numbers}')
