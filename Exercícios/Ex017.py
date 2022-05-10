co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('CUmprimento do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))
