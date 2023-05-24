#programa que leia um número inteiro e diga se ele é um número primo ou não.
num = int(input('Digite um número inteiro: '))
primos = []
for x in range(1, num + 1):
    if num % x == 0:
        primos.append(x)
if len(primos) == 2:
    print(f'{num} é um número primo.')
else:
    print(f"{num} não é um número primo")
    pass
