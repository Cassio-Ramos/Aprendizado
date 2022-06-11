km = int(input('Digite a distancia de sua viagem: '))
if km <= 200:
    print('O preço da passagem é: R$ {:2f}'.format(km*0.50))
else:
    print('O preço da passagem é: R$ {:2f}'.format(km*0.45))
