'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
soma = 0
while True:
    n = int(input('Digite um número inteiro: (cod de parada: 999) '))
    if n == 999:
        break
    soma += n
print(f'A soma de todos os valores digitados menos a flag é igual a {soma}')
