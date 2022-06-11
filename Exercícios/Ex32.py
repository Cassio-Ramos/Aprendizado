ano = int(input('Digite o ano: '))
n = ano % 4
if n == 0:
    print('O ano é Bissexto.')
else:
    print('O ano não é Bissexto. ')
