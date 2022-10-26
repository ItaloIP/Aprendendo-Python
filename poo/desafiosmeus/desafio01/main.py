import classes
produtos = []
#Produtos

produtos.append(classes.Produtos('Leite Condensado'))
produtos.append(classes.Produtos('Arroz'))

# --------------------------------------------------

print(produtos[0].nome)
while True:
    choice = int(input('''

[ 0 ] Repor estoque
[ 1 ] Novo preço 
[ 2 ] Comprar
SELECT: '''))
    if choice == 0:
        print(f'[ 0 ]{produtos[0].nome} : QUANT {produtos[0].unidades}')
        print(f'[ 1 ]{produtos[1].nome} : QUANT {produtos[1].unidades}')
        produto = int(input('Qual produto quer repor?: '))
        if produto == 0:
            produtos[0].Reposicao(int(input('Número: ')))
        elif produto == 1:
            produtos[1].Reposicao(int(input('Número: ')))
        