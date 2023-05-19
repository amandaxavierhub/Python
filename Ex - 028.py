'''Escreva um programa que faça o computador “pensar” em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
r = "S"
pontos = 0
import random
#jogador = int(input('Vamos brincar de advinhação. Diga em que número estou pensando entre 0 e 5: '))

cont = 0
pontos = 0
pc = random.randint(0,5)

while r == "S":
    jogador = int(input('Vamos brincar de advinhação. Diga em que número estou pensando entre 0 e 5: '))
    r = str(input('Gostaria de tentar mais uma vez? [S/N] ')).upper().strip()
    cont += + 1
    if jogador == pc:
        pontos += +10
    elif r !="N" and r != "S":
        print('Comando inválido.')

print(f'Vocẽ teve um total de {cont} tentativas e ganhou {pontos} pontos') 
