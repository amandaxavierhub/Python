''' Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final. Coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep

dados = {}
cont = 1
'''for c in range(0,4):
    dados['Jogador'] = randint(0,6)
    for k, v in dados.items():
        print(f'O {cont}º {k} tirou {v}')
        cont+=1'''

jogo = {
    'jogador 1': randint(1,6),
    'jogador 2': randint(1,6),
    'jogador 3': randint(1,6),
    'jogador 4': randint(1,6)
}
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
        
print('-=' * 30)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
ranking = {}

ranking =(sorted(jogo.items(), key=lambda item: item[1], reverse=True))

for i, v in enumerate(ranking):
   print(f'{i +1}º lugar: {v[0]} com {v[1]} pontos.')
   sleep(1)

