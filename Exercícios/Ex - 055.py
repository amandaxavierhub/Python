'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
maior e o menor peso lido.'''

maior = 0

for p in range(1,6):
    nome = str(input('Informe o seu nome: ')).strip()
    peso = float(input('Informe o seu peso: '))
    if peso > maior:
        maior = peso
        pesado = nome
        print(f'O maior peso até agora foi de {pesado} com {maior}')
    else:
        print(f'O menor peso até agora foi de {nome} pesa apenas {peso} kilos.')

# INCOMPLETO REVISAR
