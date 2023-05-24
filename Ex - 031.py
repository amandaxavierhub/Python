'''Desenvolva um programa que pergunte a distância de uma viagem em Km,
calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e
R$0,45 para viagens mais longas.'''

viagem = float(input('Informe a distância da viagem em Km:'))
if viagem <= 200:
    print(f'O custo total da sua viagem ficou no valor de  {viagem * 0.50}')
else:
    print(f'O custo total da sua viagem ficou no valor de {viagem * 0.40}')