'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

dados = {}
totgols = cont =0
gols = []
dados['Nome']= str(input('Nome do(a) jogador(a): '))
dados['Partida'] = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
for c in  range (dados['Partida']):
    dados['Gols'] = int(input(f'  Quantos gols {dados["Nome"]} fez na {c+1}º partida: '))
    totgols += dados['Gols']   
    gols.append(dados['Gols'])

print()
dados['Gols'] = gols
dados['Total'] = totgols
print(dados)
print('=-' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'{dados["Nome"]} jogou {dados["Partida"]} partidas.')
for c in dados['Gols']:
    print(f'    Na {cont +1}° partida fez {c} gols.')
    cont+=1
print(f'Fez um total de {dados["Total"]} gols')


