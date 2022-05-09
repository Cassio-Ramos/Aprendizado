d = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
r = (d*60)+(km*0.15)
print('O total a pagar é de R${:.2f}.'.format(r))
