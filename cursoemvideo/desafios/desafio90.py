estudante = {}
estudante['nome'] = str(input('Estudante: ')).strip()
estudante['media'] = float(input(f'Média do(a) {estudante["nome"]}: '))

if estudante['media'] >= 7:
    estudante['situação'] = 'APROVADO!'
elif 5 <= estudante['media'] < 7:
    estudante['situação'] = 'RECUPERAÇÃO!'
else:
    estudante['situação'] = 'REPROVADO!'


print('-='*20)
for k, v in estudante.items():
    print(f' - {k} é igual a {v}')
    
'''
print(f'Analise do estudante: {estudante["nome"]}')
print(f'Média = {estudante["media"]}')
print(f'Situação: {estudante["situação"]}')
'''