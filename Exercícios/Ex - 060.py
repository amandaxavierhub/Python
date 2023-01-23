#Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial

n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
while c >0:
    print(f'{c}', end=' ')
    c -= 1
print(f'O fatorial de {n} é {factorial(n)}')

# resolução 2
'''
n = int(input('Digite um númeroo para calcular o seu fatorial: '))
c = n
while c >0:
    print(f'Calculando {n}!', end='')
    print(f'x' if c > 1 else '=', end ='')
    f *= c
    c -= 1
print(f'{f}')
'''