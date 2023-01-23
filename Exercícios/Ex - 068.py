'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido 
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random
print('Vamos jogar Par ou Ímpar.')
cont = 0
while True:
    n = int(input('Escolha um número inteiro: '))
    pc = random.randint(0,10)
    tot = pc + n
    s = str(input('Par ou Ímpar? [P/I]')).upper()
    if s == 'P':
        if tot % 2 == 0:
            print('você ganhou a vez. ')
            cont += 1
        else:
            break
    elif s == 'I':
        if tot % 2 == 1:
            print('você ganhou a vez:')
            cont += 1
        else:
            break 

print(f'Você ganhou {cont} vezes consecutivas.')