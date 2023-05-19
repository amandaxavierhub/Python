''' Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadatradas;
B) Uma listagem com as pessoas mais pesadas;
C) Uma lista com as pessoas mais leves.'''

original = []
copia = []
pesado = leve = 0
while True:
    original.append(str(input('Informe o nome: ')))
    original.append(float(input('Informe o peso: Kg ')))
    if len(copia) == 0:
        pesado = leve = original[1]
    else:
        if original[1] > pesado:
             pesado = original[1]     
        if original[1] < leve:
            leve = original[1]
    copia.append(original[:])
    original.clear()
    r = int(input('[1] Cadastrar Novamente: \n[2] Finalizar Programa: '))
    if r == 2:
        break

print(f'{len(copia)} pessoas foram cadastradas.')
print(f'O maior peso cadastro foi de {pesado} Kg e pertence a  ', end='')
for c in copia:
    if c [1] ==  pesado:
        print(f'[{c[0]}]', end='')
print()
print(f'O menor peso cadastrado foi de {leve} Kg e pertence a  ', end='')
for c in copia:
    if c[1] == leve:
        print(f'[{c[0]}]', end='')
print()
print('-='*30)