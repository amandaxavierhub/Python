'''Faça um programa que tenha uma função maior() que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior (numero, lista):
    print(f'A lista de números inseridos {lista}.')
    print(f'O maior número inserido foi {numero}.')


n = []
while True:
    n.append(int(input('Informe um número inteiro: ')))
    res = str(input('Quer continuar? ')).upper()[0]
    while True:
        if res in 'SN':
            break
        else:
            print('Digite apenas "S" ou "N".')
    if res in 'N':
        break
maior(max(n), n)