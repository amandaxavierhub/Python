'''Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final,
mostre os 10 primeiros termos dessa progressão.'''

primeiro= int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 -1) * razao

for c in range (primeiro, decimo, razao):
    print(f'{c}', end=' ')