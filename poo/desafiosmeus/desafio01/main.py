import classes
#Produtos
produtos = []
produtos.append(classes.Produtos('Leite Condensado'))
produtos.append(classes.Produtos('Arroz'))

# --------------------------------------------------

print(produtos[0].nome)
while True:
    choice = int(input('''

[ 0 ] Repor estoque
[ 1 ] Adicionar novo item
[ 2 ] Novo preço 
[ 3 ] Comprar
SELECT: '''))
    if choice == 0:
        for c, v in enumerate(produtos):
            print(f'({c})R${produtos[c].preço} {produtos[c].nome} : QUANT {produtos[c].unidades}')

        produto = int(input('Qual produto quer repor?: '))
        produtos[produto].Reposicao(int(input('Quantidade à mais: ')))

    elif choice == 1:
        produtos.append(classes.Produtos(str(input('Nome do produto: '))))

    elif choice == 2:
        for c, v in enumerate(produtos):
            print(f'({c})R${produtos[c].preço} {produtos[c].nome}')

        produto = int(input('Qual produto quer alterar o preço?: '))
        produtos[produto].NewPrice(float(input(f'Novo preço do(a) {produtos[produto].nome}: R$')))

    elif choice == 3:
        for c, v in enumerate(produtos):
            if produtos[c].unidades > 0 and produtos[c].preço > 0:
                print(f'({c}){produtos[c].nome} por R${produtos[c].preço}')
                comprar = int(input('Qual item deseja comprar?: '))
                uni = int(input('Quantas quantidades?: '))
                try:
                    produtos[comprar].Comprar(uni)
                except:
                    print('Algo deu errado!')
                else: 
                    print('Compra feita!')
                
