#escreva 5 valores e compare o maior e o menor

pos = maior = menor = 0

numbers = [1,5,1,4,5]
#for num in range(0,5):
#    numbers.append(int(input(f'Digite um número para a posição {pos}: ')))
#    pos += 1

maior = numbers[:]
menor = numbers[:]

maior.sort(reverse=True)
menor.sort()


print('='*24)
print(f'Você digitou os valores {numbers}')
print(f'O maior número encontrado foi o {max(numbers)} na posição {numbers.index[max(numbers)]}', end=' ')




print(f'\nO menor número encontrado foi o {min(numbers)}')
