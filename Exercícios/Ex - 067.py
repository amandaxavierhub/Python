''' Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando
 o número solicitado for negativo.'''

while True:
    n = int(input('Digite um número inteiro para descobrir sua tabuada: '))
    if n <= 0:
        break
    for c in range (1,12 -1):
        t = c * n
        print(f'{n} x {c} = {t}')
    