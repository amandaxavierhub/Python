'''Desenvolva um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz com a formatação correta.'''

original = []
copia = []

for c in range (0,9):
    original.append(int(input('Insira um número inteiro: ')))
    copia.append(original[:])
    original.clear()
for c in copia[:3]:
    print(f'{c}', end=' ')
print()
for c in copia[3:6]:
    print(f'{c}', end=' ')
print()
for c in copia[6:]:
    print(f'{c}', end=' ')

