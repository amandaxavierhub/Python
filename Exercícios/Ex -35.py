#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo.



reta1 = float(input('Informe o comprimento da primeira reta: '))
reta2 = float(input('Informe o comprimento da segunda reta: '))
reta3 = float(input('Informe o comprimento da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'Os segmentos formam um triângulo.')
else:
    print(f'Os segmentos não formam um triângulo.')