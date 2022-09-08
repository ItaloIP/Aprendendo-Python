#escreva 5 valores e compare o maior e o menor

pos = 0
maior1 = menor1 = 0

numbers = list()

for num in range(0,5):
    numbers.append(int(input(f'Digite um número para a posição {pos}: ')))
    pos += 1
    
maior = max(numbers)
menor = min(numbers)


print('='*24)
print(f'Você digitou os valores {numbers}')

print(f'O maior número encontrado foi o {maior} na posição ')

    
print(f'\nO menor número encontrado foi o {menor} na posição ', end=' ')
