nome = str(input('Qual o seu nome?: ')).strip().capitalize()
if nome == 'Italo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino')    
else:
    print('Seu nome é bem normal!')
print('Olá, {}!'.format(nome))
