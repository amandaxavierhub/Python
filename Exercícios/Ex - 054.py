'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.'''

from datetime import date
cont = 0
cont1 = 0
for d in range (1,8 ):
    nas = int(input('Informe o seu ano de nascimento: '))
    idade = date.today().year - nas
    if idade >=21:
        cont += 1
    else:
        cont1 += 1
print(f'{cont} pessoas ainda são menores de 18 anos e {cont1} já estão na maioridade.')