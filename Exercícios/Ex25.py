nome = str(input('Qual seu nome completo? ')).strip()
m = nome.upper()
print('Seu nome tem Silva? {}'.format(m.find('SILVA') > 0))
