import random
from time import sleep


# inicio game
name = str(input('Bem-Vindo ao game JokenPô. Digite o seu nome para começar:\n '))

print(f'''Olá {name}! Seu adversário será MK. Divirta-se! ''')
sleep(0.7)
resposta = "S"
score = 0
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

    if pc == 1:
        if player == 1:
            print('Empate.')
            score += 1
        if player == 2:
            print(f'{name} ganhou a rodada')
        if player == 3:
            print('Pc ganhou a rodada.')

    if pc == 2:
        if player == 1:
            print('Pc ganhou a rodada.')
        if player == 2:
            print('Empate,')
        if player == 3:
            print(f'{name} ganhou a vez.')
            score += 1
    
    if pc == 3:
        if player == 1:
            print(f'{name} ganhou a rodada.')
            score += 1
        if player == 2:
            print('Pc ganhou a rodada')
        if player == 3:
            print('Empate')
    resposta = str(input('Gostaria de tentar novamente? [S/N]')).upper()
    if resposta == "S":
        cont += 1

    
print(f'Você fez um total de {score} num total de {cont + 1} tentativas.')
