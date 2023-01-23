'''Crie um programa onde o  usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

lista = [[], []]

for c in range (0,7):
    valor = (int(input(f'Digite o {c +1} valor: ')))
    if valor % 2 ==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print(f'Os valores pares digitados foram {sorted(lista[0])}')
print(f'Os valors ímpares digitados foram {sorted(lista[1])}')

'''lista = []
for c in range(0,7):
    valor = int(input(f'Informe o {c+1}° valor: '))

    lista.append(valor)
lista.sort()
print(f'Os números pares da lista são: ', end= ' ')
for c in lista:
    if c % 2 == 0:
        print(f'{c}', end=', ')
print(' ')
print(f'Os números ímpares da lista são:', end=' ')
for c in lista:
    if c % 2 ==1:
        print(f'{c}', end=', ')
print(' ')      
print('='* 30)'''

