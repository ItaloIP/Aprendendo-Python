from random import randint


numbers = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), 
            randint(0,10))

print(f'Os números sorteados foram {numbers}')
 
print(f'O maior número é o {max(numbers)}')
print(f'O menor número é o {min(numbers)}')
