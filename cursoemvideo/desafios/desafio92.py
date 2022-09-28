from datetime import date, datetime
trabalhador = dict()

# ---- # 

while True:
    trabalhador['Nome'] = str(input('Nome: ')).strip()
    nascimento = int(input('Ano de nascimento: '))
    trabalhador['Idade'] = date.today().year - nascimento
    trabalhador['ctps'] = int(input('Cód da carteira de trabalho (caso não tenha, digite 0): '))

    if trabalhador['ctps'] == 0:
        print('-='*20)
        for c, k in trabalhador.items():
            print(f'   - {c} tem o valor: {k}')
        break
    else:
        trabalhador['Contratação'] = int(input('Ano de contratação: '))
        trabalhador['Salário'] = float(input('Salário: '))
        trabalhador['Aposentadoria'] = trabalhador['Idade'] + ((trabalhador['Contratação'] + 35) - datetime.now().year)
        print('-='*20)
        for c, k in trabalhador.items():
            print(f'   - {c} tem o valor: {k}')
        break