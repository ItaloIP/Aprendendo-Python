maior1 = menor1 = 0
numbers = []
for num in range(0,5):
    numbers.append(int(input(f'Digite um número para a posição {num}: ')))
maior = max(numbers)
menor = min(numbers)

print('='*24)
print(f'Você digitou os valores {numbers}')
print(f'O maior número encontrado foi o {maior} nas posições: ', end='')
for t, v in enumerate(numbers):
    if v == maior:
        print(t,end='... ')
print(f'\nO menor número encontrado foi o número {menor} nas posições: ', end='')
for t, v in enumerate(numbers):
    if v == menor:
        print(t,end='... ')
