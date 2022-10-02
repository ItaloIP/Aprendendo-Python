grupo = list()
pessoa = dict()
mulheres = list()
acmedia = list()


vivo = soma = 0
# --- #

while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro! Apenas M ou F.')
    ano = int(input('Idade: '))
    pessoa['idade'] = ano

    
    grupo.append(pessoa.copy())
    pessoa.clear()
    soma += ano
    ano = 0
    vivo += 1

    choice = str(input('Quer cadastrar mais pessoas? [S/N]: ')).strip().upper()[0]
    if choice in 'SN': 
        if choice == 'N':
            break
        print('-='*20)
    else:
        while True:
            choice = str(input('Erro! Quer cadastrar mais pessoas?[S/N]: ')).strip().upper()[0]
            if choice in 'SN':
                break
        if choice == 'N':
            break

media = soma / vivo
print('-='*30)

print(f'Há {len(grupo)} cadastradas.')
print(f'A média de idade destas pessoas é {media}')
print(f'As mulheres cadastradas foram: ',end='')
for v in grupo:
    if v['Sexo'] == 'F':
        print(f'{v["Nome"]}, ', end='')
print()
print(f'Pessoas que estão acima da média:',end='')
for p in grupo:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()