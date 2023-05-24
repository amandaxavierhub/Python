#Crie um programa que faça o computador jogar Jokenpô com você.

# importando bibliotecas

import random
from time import sleep

# inicio game
name = str(input('Bem-Vindo ao game JokenPô. Digite o seu nome para começar:\n '))

print(f'''Olá {name}! Seu adversário será MK. Divirta-se! ''')
sleep(0.7)
resposta = "S"
score = 10
cont = 0
while resposta == "S":
   
    print('''=================================
    1 - Pedra
    2 - Papel
    3 - Tesoura
    ''')
    pc = random.randint(1,3)
    print(f'Mk{pc} ')
    player = int(input('Faça a sua escolha: '))
    
    print('Jo')
    sleep(1)
    print('Ken')
    sleep(1)
    print('Pô')

    if player ==1 and pc == 2:  # pedra x papel
        print('Pc ganhou a rodada:')
        cont += + 1 
    if pc ==1 and player ==2: # pedra x papel
        print(f'{name} ganhou a rodada') 
        score =+  1
        cont += + 1

    if player ==1 and pc == 3: # pedra x tesoura
        print(f'{name} venceu a rodada')
        score +=  1
        cont += + 1
    if pc ==1 and player ==3: # pedra x tesoura
        print(f'Pc ganhou a rodada.')
        cont += 1 

    if player ==2 and pc == 3: # papel x tesoura
        print('Pc ganhou a rodada.')
        cont += + 1 
    if pc ==2 and player == 3: # papel x tesoura
        print(f'{name} ganhou a rodada.')
        score =+  1
        cont += + 1 

    if player == 3 and pc == 1:  # tesoura x papel
        cont += + 1 
    if pc == 3 and player == 1: # tesoura x papel
        score =+  1

    if pc == player: # empate
        print('Empate.')
        cont += + 1 
      
    resposta = str(input('Gostaria de tentar novamente? [S/N]')).upper()

    
print(f'Você fez um total de {score} score num total de {cont} tentativas.')
