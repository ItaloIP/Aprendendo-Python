p20 = ('Palmeiras','Santos','Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians', 'Internacional', 'Cruzeiro', 'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Flumimnense', 'Coritiba', 'Bahia', 'Goiás', 'Guarani', 'Sport', 'Portuguesa', 'Atlético Paranaense', 'Vitória')
print(f'Lista de Times do Brasileirão: {p20}')
print('-='*30)

#5 Primeiros Colocados
print(f'Os 5 primeiros colocados do Brasileirão são: {p20[0:5]}')
print('-='*30)

#4 Últimos
print(f'Os 4 últimos são: {p20[-4:]}')
print('-='*30)

#Ordem Alfabética
print(f'Times em ORDEM ALFABÉTICA: {sorted(p20)}')
print('-='*30)

#Onde está o Flamengo
flameng = p20.index('Flamengo')+1
print(f'O Flamengo está em {flameng}o')
print('-='*30)
