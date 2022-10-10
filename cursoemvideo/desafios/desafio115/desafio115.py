from utilidades import arquivo
from utilidades import interface, arquivo
from time import sleep

arq = 'pessoas.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)


while True:
    resposta = interface.menu(['Cadastrar', 'Listar', 'Sair'])
    if resposta == 1:
        interface.tit('Novo cadastro')
        nome = str(input('Nome: '))
        idade = interface.Opc('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 2:
        interface.tit('Opção 2')
        arquivo.lerArquivo(arq)
    elif resposta == 3:
        print('Saindo do programa.')
        break
    else:
        print('\033[31mDigite uma opção válida!')
    sleep(1.7)
