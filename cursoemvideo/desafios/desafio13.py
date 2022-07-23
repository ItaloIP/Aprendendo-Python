s = float(input('Quanto que é seu salário?'))
a = float(input('Pretende ter quantos porcento de aumento? % '))
st = s + (s * a / 100)
print('Ao total, seu salário com {:.2f}% de aumento ficaria de {:.2f}'.format(a,st))