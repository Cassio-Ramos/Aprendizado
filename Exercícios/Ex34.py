salario = float(input('Digite seu salário: '))
if salario <= 1250.0:
    print('Seu aumento foi de 15% (R$ {:.2f}), seu novo salário é: R$ {:.2f}.'.format(salario*.15, salario*1.15))
else:
    print('Seu aumento foi de 10% (R$ {:.2f}), seu novo salário é: R$ {:.2f}.'.format(salario * .10, salario*1.10))
