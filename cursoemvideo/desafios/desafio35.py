m1 = float(input('Digite a primeira medida: '))
m2 = float(input('Digite a segunda medida: '))
m3 = float(input('Digite a últilma medida: '))
'''
maior = m1
if m2>m1 and m2>m3:
    maior = m2
if m3>m1 and m3>m2:
    maior = m3

menor = m1 + m2
if m2 + m3 < m1:
    menor = (m2 + m3)
if m1 + m3 < m2:
    menor = (m1 + m3)
'''

if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print('As medidas acima PODEM FORMAR UM TRIÂNGULO')
else:
    print('As medidas acima NÃO PODEM FORMAR UM TRIÂNGULO')
print('FIM')
 