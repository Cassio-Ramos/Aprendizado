import random
n = random.randint(1, 5)
e = int(input('Digite um número de 1 à 5: '))
print('A escolha do programa foi {}, desta forma:'.format(n))
if e == n:
    print('Você ganhou! ')
else:
    print('Você perdeu! ')
