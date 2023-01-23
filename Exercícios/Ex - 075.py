'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9;
B) Em que posição foi digitado o primeiro valor 3;
C) Quais foram os números pares.'''
cont = 0
n = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')))

print(f'o número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O primeiro número 3 foi digitado na {n.index(3)+1}° posição')
else:
    print('O númeoro 3 não foi digitado.')
print('Os números pares digitados foram: ', end= '')

for c in n:
    if c % 2 ==  0:
        print(c,end=' ')
