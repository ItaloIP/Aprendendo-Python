from utilidades import interface


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Ocorreu um erro')
    else:
        interface.tit('Pessoas Cadastradas!')
        print(a.readlines())