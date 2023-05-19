'''– Faça um programa que tenha uma função chamada área que receba as dimensões do terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area (l , c):
    print('=-' * 20)
    terreno = l * c
    print()
    print(f'A área do terreno é de {terreno}m².')
    print()
    print('=-' * 20)


print('Informe os dados para saber qual a área do terreno.')
largura = float(input('Largura(m): '))
comprimento = float(input('Comprimento(m): '))
area(largura, comprimento)