estudante = {}
estudante['nome'] = str(input('Estudante: '))
estudante['media'] = float(input(f'Média do(a) {estudante["nome"]}: '))

print('-='*20)

print(f'Analise do estudante: {estudante["nome"]}')
print(f'Média = {estudante["media"]}')
print(f'Situação: ', end='')
if estudante['media'] >= 6:
    print('APROVADO')
else:
    print('REPROVADO')
