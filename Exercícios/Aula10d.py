nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))
media = (nota_1 + nota_2)/2
print('Sua média foi {:.2f}, desta forma: '.format(media))
print('Você foi aprovado.'if media >= 6 else 'Você reprovou.')
