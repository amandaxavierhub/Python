# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente desse ângulo.

import math

angulo = float(input('Informe o ângulo: '))
# convertendo o valor em radiano
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno do ângulo {angulo} é {seno :.2f}, o cosseno é {cosseno :.2f} e a tangente é {tangente :.2f}' )
