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
        for lin in a:
            dado = lin.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3}')
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Ocorreu algum erro.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO em cadastrar uma pessoa!')
        else:
            print(f'Novo registro de {nome}')
            a.close()