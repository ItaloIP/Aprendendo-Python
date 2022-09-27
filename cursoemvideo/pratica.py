pessoas = {'nome': 'Italo', 'sexo':'M', 'idade': 16}
pessoas['peso'] = 47.5
#del pessoas['sexo']
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.keys())
for k, v in pessoas.items():
    print(f'{k} = {v}')