tupla = ('ESTUDAR', 'APRENDER', 'IMPORTANTE', 'DORMIR', 'ESTRUTURA', 'GRÁTIS')

for c in tupla:
    print(f'\nNa palavra {c} temos as vogais: ',end=' ')
    for vogal in c:
        if vogal in 'A,Á,À,E,É,È,I,Í,Ì,O,U':
            print(f'{vogal.lower()}', end=' ')
