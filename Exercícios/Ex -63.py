'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os
n primeiros elementos de uma sequência de Fibonacci.
Ex: 0 -1-1-2-3-5-8...'''

print(' Sequência de Fibonacci')

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print(f'⇨ {t1} ⇨ {t2}', end=' ')
while cont <= n:
    t3 = t1 + t2
    print(f' ⇨ {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('')
print('Fim')
