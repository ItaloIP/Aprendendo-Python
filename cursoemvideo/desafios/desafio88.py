from random import sample
import time

sorteios = []
print('='*50)
print(f'{"JOGO DA MEGA SENA":^50}')
print('='*50)
n = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, n):
    sorteios.append(sorted(sample(range(1, 61), 6)))
print('='*50)
print(f'Os sorteios dos {n} jogos são os seguintes:')
for a, b in enumerate(sorteios):
    time.sleep(1)
    print(f'JOGO {a + 1}: {b}')
time.sleep(1)
print('='*50)
