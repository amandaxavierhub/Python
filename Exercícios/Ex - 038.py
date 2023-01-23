'''Escreva um programa que leia dois números inteiros e compra-os mostrando na
tela uma mensagem:
•
•
•
O primeiro valor é o maior;
O segundo valor é o maior;
Não existe valor maior, os dois são iguais.'''

from binascii import Incomplete


primeiro = int(input('Informe o primeiro valor: '))
segundo = int(input('Informe o segundo valor:  '))
if primeiro > segundo:
    print(f'O primeiro valor = {primeiro} é o maior valor: ')
elif segundo > primeiro:
    print(f'O segundo valor =  {segundo} é o maior valor:')
else:
    print('Não existe maior valor. Os dois são iguais.')
