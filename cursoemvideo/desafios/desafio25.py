#Se há Silva no Nome completo
name = str(input('Digite seu nome completo: ')).upper().strip()
sobrenome = 'SILVA' in name
print('Seu nome têm Silva? {}'.format(sobrenome))
