'''Crie uma tupla prenchida com os 20 primeiros colocados na tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A)  Apenas os 5 priemiros colocados;
B) Os últimos 4 colocados;
C) Uma lista com os times em ordem alfabética
D) Em que posição da tabela está o time da Corinthians.
'''
times = (
    'Palmeiras ............42 pts',
    'Corinthians ..........38 pts',
    'Fluminense ...........35 pts',
    'Athletico-PR .........34 pts',
    'Flamengo .............33 pts',
    'Internacional ........33 pts',
    'Atlético-MG ..........32 pts',
    'Bragantino ...........32 pts',
    'Santos ...............27 pts',
    'São Paulo ............26 pts',
    'Goiás ................25 pts',
    'Botafogo .............24 pts',
    'América-MG ...........24 pts',
    'Ceará SC .............24 pts',
    'Coritiba .............22 pts',
    'Avaí .................21 pts',
    'Cuibá ................20 pts',
    'Fortaleza ............18 pts',
    'Atlético-GO ..........17 pts',
    'Juventude ............16 pts',
)
lista = [times]

print('='*40)
print(' \033[1;32m Classificação Campeonato Brasileiro.\033[m\n ')
for c in times:
    print(f'\033[1;33m {c}\033[m')
print('='*40)
print()
print('\033[1;32m Os 5 primeiros colocados são ➡\033[m\n')
for c in times[0:6]:
    print(f'\033[1;36m {c} \033[m')
print('='*40)
print()
print('\033[1;32m Os 4 últimos colocados são ➡ \033[m\n')
for c in times[16:]:
    print(f'\033[1;31m {c} \033[m')
print('='*40)
print()
print('\033[1;32m Os times em ordem alfabética ➡ \033[m\n')
for c in sorted(times[0:]):
    print(f'\33[1;34m {c} \033[m')
print('='*40)
print()
print(f'\033[33mO time Corinthianas se encontra na {times.index("Corinthians ..........38 pts")+1}° posição.\033[m')
print('='*40)