#Radar
run = float(input('Qual a velocidade do carro que passou agora na estrada?:Km/H: '))
cal = (run - 80) * 7.00 #Cálculo
if run > 80:    #Se o carro passar acima de 80Km/H
    print('O carro recebeu R${:.2f} de multa por estar acima de 80Km/h.'.format(cal))
else:
    print('Ok')
print('--FIM--')
