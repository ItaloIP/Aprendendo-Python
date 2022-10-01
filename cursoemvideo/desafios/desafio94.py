import enum


grupo = list()
pessoa = dict()
mulheres = list()
acmedia = list()
sexos = ''

vivo = soma = 0
# --- #

while True:
    pessoa['Nome'] = str(input('Nome: '))
    sexos = str(input('Sexo [M/F]: ')).strip().upper()
    if sexos == 'M':
        pessoa['Sexo'] = sexos 
        sexos = ''
    elif sexos == 'F':
        mulheres.append(pessoa['Nome'])
        pessoa['Sexo'] = sexos 
        sexos = ''
    else:
        while True:
            sexos = str(input('Tente novamente! [M/F]: ')).strip().upper()
            if sexos == 'M':
                pessoa['Sexo'] = sexos 
                sexos = ''
                break
            elif sexos == 'F':
                mulheres.append(pessoa['Nome'])
                pessoa['Sexo'] = sexos 
                sexos = ''
                break
    ano = int(input('Idade: '))
    pessoa['idade'] = ano

    
    grupo.append(pessoa.copy())
    pessoa.clear()
    soma += ano
    ano = 0
    vivo += 1

    choice = str(input('Quer cadastrar mais pessoas? [S/N]: ')).strip().upper()
    if choice in 'SN': 
        if choice == 'N':
            break
        print('-='*20)
    else:
        while True:
            choice = str(input('Erro! Quer cadastrar mais pessoas?[S/N]: ')).strip().upper()
            if choice in 'SN':
                break
        if choice == 'N':
            break

media = soma / vivo
for c, v in enumerate(grupo):
    for a, b in enumerate(v.items()):
        print(b['Idade'])

    # if v[c][2] > media:
    #     acmedia.append(v)
# print(grupo)
# print(acmedia)
print('-='*30)

print(f'Há {vivo} cadastradas.')
print(f'A média de idade destas pessoas é {media}')
print(f'As mulheres cadastradas foram: ',end='')
for c, v in enumerate(mulheres):
    print(f' {v},', end='')
print(f'Pessoas que estão acima da média:',end='')
print('')
print('')
for c, v in enumerate(acmedia):
    print(f'nome = {acmedia[0]}; sexo = {acmedia[1]}; idade = {acmedia[2]}')
