def Notas(*notas, obv=False):
    """
    -> Função para calcular *LER  QUANTAS NOTAS; * QUAL A MAIOR NOTA E A MENOR; *MÉDIA; *Situação do aluno(Opcional)
    :param *notas: Empacotar os valores
    :param obv: (opcional) revela a situação do aluno
    :return: Sim, retorna um dicionário
    """
    num = 0
    nota = notas
    boletim = {}
    boletim['Total'] = len(notas)
    boletim['Maior nota'] = max(notas)
    boletim['Menor nota'] = min(notas)
    boletim['Média'] = sum(notas) / len(notas)
    if obv == True:
        if boletim['Média'] < 5:
            boletim['Situação:'] = 'Péssimo!'
            return boletim            
        elif 5 > boletim['Média'] < 6:
            boletim['Situação:'] = 'Na média!'
            return boletim
        elif boletim['Média'] > 8:
            boletim['Situação:'] = 'Boa!'
            return boletim
        else:
            boletim['Situação:'] = 'Perfeito!'
            return boletim       
    else:
        return boletim     



#programa principal
aluno = Notas(5.5, 2.5, 1.5, obv=False)
print(aluno)
