'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km = float(input('Informe quantos Km percorreu: KM '))
day = int(input('Quantidade de dias alugado: '))
  
price = (day * 60) + (km * 0.15) 
print(f'Você percorreu {km} e alugou o carro por {day}, o preço final do aluguel foi de {price}')
