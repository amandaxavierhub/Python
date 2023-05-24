'''Escreva um programa que leia a velocidade de um carro. Se ela ultrapassar
80Km/hm, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
R%7,00 por cada Km acima do limite.'''


velocidade = float(input('Informe a velocidade do seu carro: Km/h '))
multa = velocidade - 80
print(f'Você ultrapassou o limite de velocidade estipulado de 80 km/h e a sua multa é de R${multa * 7}.')
