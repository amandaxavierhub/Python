'''Crie um programa que leia vários números inteiros pelo teclado. No final da
execução, mostre a média entre todos os valores e qual foi o maior e o menor valores
lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar
valores.'''

from ast import Num


media = 0
soma = 0
cont = 0
res = "S"
maior = menor = 0
while res == "S":
    n = int(input('Digite um número inteiro: '))
    res = str(input('Gostaria de inserir novos valores? [S/N] ')).upper()
    soma += n
    cont += 1
    if cont ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'O maior valor inserido foi {maior} \n O menor valor inserido foi  {menor}')
print(f'A soma de todos os valores inseridos é = {soma}')
print(f'A média de todos os valores inseridos é {soma / (cont-1):.2f}')