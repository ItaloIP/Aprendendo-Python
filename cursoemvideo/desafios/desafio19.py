import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
students = [a1,a2,a3,a4]

choice = random.choice(students)

print('O aluno escolhido foi {}.'.format(choice))
