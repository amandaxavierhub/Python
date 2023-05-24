'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
Ps: criar uma interface para esse programa
'''

from random import shuffle
from time import sleep
megasena = list(range(0,61))
print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
pergunta = int(input('Quantos números quer que eu sorteie? '))
for aposta in range(1, pergunta+1):
    print(f'Jogo {aposta}: ', end='')
    sleep(1)
    shuffle(megasena)
    print(megasena[:6])
    del(megasena[:6])
