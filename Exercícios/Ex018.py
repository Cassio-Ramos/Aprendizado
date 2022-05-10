import math
n1 = float(input('Digite um angulo: '))
n = math.radians(n1)
sen = math.sin(n)
cos = math.cos(n)
tan = math.tan(n)
print('O valor de seno é {:.2f}\nDe cosseno é {:.2f}\ne o da tangente é {:.2f}'.format(sen, cos, tan))
