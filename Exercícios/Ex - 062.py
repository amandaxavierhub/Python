'''Melhore o desafio 61, perguntando se ele quer mostrar mais alguns termos. O
programa encerra quando ele disser que quer mostrar 0 termos.'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
res = 10
tot = 0
while res != 0:
    tot += res
    while c <= tot:
        print(f'{termo} ->', end='')
        termo += razao
        c += 1
    print('')
    res = int(input('Quantos termos você quer mostrar a mais? '))
print('Finalizando programa.')