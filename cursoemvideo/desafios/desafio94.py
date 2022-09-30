grupo = []
pessoa = {}
mulheres = []
sexos = ''
vivo = soma = 0
# --- #

while True:
    pessoa['Nome'] = str(input('Nome: '))
    sexos = str(input('Sexo [M/F]: ')).strip().upper()
    if sexos in 'MF':
        pessoa['Sexo'] = sexos 
        sexos = ''
    if sexos == 'F':
        mulheres.append(pessoa['Nome'])
        grupo.append(mulheres[:])
        mulheres.clear()
    else:
        while True:
            sexos = str(input('Tente novamente! [M/F]: ')).strip().upper()
            if sexos in 'MF':
                pessoa['Sexo'] = sexos 
                grupo.append(mulheres[:])
                mulheres.clear()
            if sexos == 'F':
                mulheres.append(pessoa['Nome'])
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

print('-='*30)

print(f'Há {vivo} cadastradas.')
print(f'A média de idade destas pessoas é {media}')
print(f'As mulheres cadastradas foram: 'end= '')
for c, v in 

    