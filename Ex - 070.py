'''Crie um programa que  leia o nome e o preço de vários produtos.
 O programa deverá perguntar 
se o usuário vai continuar. No final, mostre: 
A) Qual é o total gasto na compra;
B) Quantos produtos custam mais de R$1000;
C) Qual o nome do produto mais barato.'''

produtos = total = menor = c =0
barato = ''

while True:
    nome = str(input('Informe o nome do produto: ')).split()
    preco = float(input('Informe o valor do produto: '))
    c += 1 # contador de ordem dos produtos
    total += preco
    if preco > 100:
        produtos +=1
    if c ==1: # se contador = 1 
        menor = preco  # menor recebe o preço
        barato = nome
    else:
        if preco < menor: # se o preço for menor que o valor gravado em 'menor'
            menor = preco #menor recebe preco
            barato = nome
    resposta = str(input('Gostaria de continuar:[S/N] ')).upper()
    if resposta == "N":
        break

print(f'O total gasto na compra foi R${total}')
print(f'No total {produtos} produtos custaram mais de R$1000. ')
print(f'O item mais barato foi {barato} no valor de {menor:.2f}.')
