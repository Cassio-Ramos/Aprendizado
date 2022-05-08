n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
rd = n1 % n2
print('A soma é \n {}.'.format(s), end=' ')
print('A divisão é {:.2f}.'.format(d))
print('A múltiplicação é {}'.format(m))
print('A divisão inteira é {}'.format(di))
print('O resto da divisão é {}'.format(rd))