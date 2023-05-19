'''Faça um programa que tenha uma função chamada contador() que receba três parâmetros: inicio, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1.
B) De 10 até 0, de 2 em 2.
C) Uma contagem personalizada.'''

from time import sleep
def contador (i, f, p):
    if p <0:
        p *=-1 # Invertendo o sinal do passo
    if p ==0:
        p = 1 # Não existe passo 0, então tornamos a opção 0 em passo 1
    print(f'Contangem de {i} até {f} pulando de {p} em {p}')
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont +=p
        print('')
    elif i > f:
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont+=p
contador(1,10,1)
contador(0, 10, 2)
print('-'*20)
print('Escolha como será a contagem.')
ini = int(input('Inicio:'))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)