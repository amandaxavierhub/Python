'''Ex 93 --> Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogadoru. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
time = []
jogador = {}
gols = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador(a): '))
    partida = int(input(f'  Quantas partidas {jogador["Nome"]} jogou? '))
    gols.clear()
    for c in range(0,partida):
        gols.append(int(input(f'Quantas gols {jogador["Nome"]} fez na {c+1}° partida? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        res = str(input('Quer continuar [S/N]? ')).upper()[0]
        if res in "SN":
            break
        else:
            print('Digite apenas S ou N.')
    if res in "Nn":
        break
print()
print('Cod', end='')
for i in jogador.keys():
    print(f' {i:<13}', end='')
print()
print('-'*40)
for k , v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Exibir dados de qual jogador? (999) interrompre. '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro de código.')
    else:
         print(f' Levantamento do jogador {time[busca]["Nome"]}')
         for i , g in enumerate(time[busca]['Gols']):
            print(f'    Na {i+1}° partida fez {g} gols')
print('----- FINLIZANDO PROGRAMA -----')
