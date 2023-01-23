''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas 
posições na lista.
'''

lista = []

for valor in range (0,5):
    lista.append(int(input('Digite um valor:')))
print(f'Os valores digitados foram {lista}')
if lista.count(max(lista)) == 1:
    print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista)) +1} ')
else:
    print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')  
    for indice, valor in enumerate(lista):
        if valor == max(lista):
            print(f'{indice + 1}... ', end='')
print('')

if lista.count(min(lista)) == 1:
    print(f'O menor valor digitado foi {min(list)} na posição {lista.index(min(lista)) +1}')
else:
    print(f'O menor valor digitado foi {min(lista)} na posições ', end='')
    for indice, valor in enumerate(lista):
        if valor == min(lista):
            print(f'{indice + 1} ...', end='')