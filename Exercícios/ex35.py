r1 = float(input('Digite o Primeiro seguimento: '))
r2 = float(input('Digite o Segundo seguimento '))
r3 = float(input('Digite o Terceiro seguimento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triangulo!')
else:
    print('Os seguimentos acima NÂO podem formar um triangulo!')
