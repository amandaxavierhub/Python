'''Melhore o jogo do desafio 28 onde o computador vai “pensar” em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no
final quantos palpites foram necessários para vencer.'''

import random
pc = random.randint(0,10)
print(pc)
res = 0
cont = 1
while res != pc:
    res = int(input('Escolha um número entre 0 e 10: '))
    if res != pc:
        cont += 1

print(f'Você teve um total de  {cont} tentativas.')

