'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.'''

frase = str(input('Escreva uma frase qualquer: '))
palavras = frase.split()  #criando uma lista
juntos = ''.join(palavras) # juntanto as palavras
inverso = juntos[:: -1] # pegando da última letra até a primeira -1

print(f'O inverso de {juntos} é {inverso} ')
if inverso == juntos:
    print('Temos um palíndromo.')
else:
    print('A frase não é um palíndromo.')