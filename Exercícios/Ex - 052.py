'''Faça um programa que leia um número inteiro e diga se ele é ou não um número
primo.'''

num = int(input('Digite um número inteiro qualquer: '))
primos = []
for x in range(1, num, + 1):
    if num % x == 0:
        primos.append(x)
if len(primos) ==2:
        print(f'{num} é um número primo!')
else:
        pass
# revisar exercicio