km = int(input('Digite sua velocidade média: '))
if km > 80:
    print('O valor da sua multa é R$ {}!'.format((km-80) * 7))
else:
    print('Não há multa a ser aplicada!')
    