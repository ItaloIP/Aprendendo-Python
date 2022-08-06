#calcular seno, cosseno e tangente
from math import sin, cos, tan, radians

área = float(input('Informe uma área '))
sen = sin(radians(área))
cos = cos(radians(área))
tan = tan(radians(área))
print('O SENO é {:.2f}\n o COSSENO é {:.2f}\n a TANGENTE é {:.2f}.'.format(sen,cos,tan))
