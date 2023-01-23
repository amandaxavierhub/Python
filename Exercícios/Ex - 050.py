'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que foram pares. Se o valor digitado for ímpar, desconsidero-o.'''
soma = 0
for n in range (1,7):
    n = int(input('Digite um número inteiro'))
    if n %2 ==0:
        soma += n
print(f'A soma de todos os números pares é = {soma}')