import classes
from time import sleep

tokem = '1234'
#Produtos
produtos = []

# --------------------------------------------------

while True:
    choice = int(input('''
----------------------------------------- 
[ 0 ] Repor estoque (only admin)
[ 1 ] Adicionar novo item (only admin)
[ 2 ] Novo preço (only admin)
[ 3 ] Comprar
[ 4 ] Visualizar (only admin)
SELECT: '''))
    if choice == 0:
        password = str(input('Digite a senha: '))
        sleep(1)
        if password == tokem:
            try:
                for c, v in enumerate(produtos):
                    print(f'\n({c}) R${produtos[c].preço} {produtos[c].nome} : QUANT {produtos[c].unidades}')
                produto = int(input('\nQual produto quer repor?: '))
                produtos[produto].Reposicao(int(input('\nQuantidade à mais: ')))
            except:
                print('Algo deu errado!')
        else: 
            print('Senha incorreta!')

    elif choice == 1:
        sleep(1)
        password = str(input('Digite a senha: '))
        if password == tokem:
            produtos.append(classes.Produtos(str(input('Nome do produto: '))))
        else: 
            print('Senha incorreta!')

    elif choice == 2:
        password = str(input('Digite a senha: '))
        if password == tokem:
            for c, v in enumerate(produtos):
                print(f'({c}) R${produtos[c].preço} {produtos[c].nome}')
                sleep(2)
            try:
                produto = int(input('\nQual produto quer alterar o preço?: '))
                produtos[produto].NewPrice(float(input(f'\nNovo preço do(a) {produtos[produto].nome}: R$')))
            except:
                print('Algo deu errado!')
        else: 
            print('Senha incorreta!')

    elif choice == 3:
        for c, v in enumerate(produtos):
            if produtos[c].unidades > 0 and produtos[c].preço > 0:
                print(f'\n({c}) {produtos[c].nome} por R${produtos[c].preço}')
                sleep(2)
                comprar = int(input('Qual item deseja comprar?: '))
                uni = int(input('Quantas quantidades?: '))
                try:
                    produtos[comprar].Comprar(uni)
                except:
                    print('Algo de errado ocorreu!')
                else: 
                    print('Compra feita com sucesso!')

    elif choice == 4:
        password = str(input('Digite a senha: '))
        if password == tokem:
            for c, v in enumerate(produtos):
                print(f'({c}) R${produtos[c].preço} {produtos[c].nome} : QUANT {produtos[c].unidades}')
                sleep(4.5)
        else: 
            print('Senha incorreta!')
            sleep(2)
    else:
        print('ERRO! Opção inválida!')
        sleep(2)

