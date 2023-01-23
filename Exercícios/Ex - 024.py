#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
#com o nome “Santo
from time import sleep
city = str(input('Informe o nome da sua cidade: ')).title()
print('Analisando se sua cidade tem o nome "Santo"\n...')
sleep(2)
if city [0:5] == "Santo" or "Santos":
    print(f'Sua cidade se chama {city} e possui a palavra "Santo/Santos".')
else: 
    print(f'Sua cidade se chama {city} e não possui a palavra Santo e esta na posição ')
