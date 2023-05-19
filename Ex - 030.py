#Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é
#par ou ímpar.

num = int(input('Digite um número inteiro qualquer: '))
if num % 2 == 0:
    print(f'{num} é um número par.')
else:
    print(f'{num} é um número ímpar.')
