'''Refaça o desafio 35 dos triângulos. Acrescentando o recurso de mostrar que tipo
de triângulo será formado:
Equilátero: Todos os lados iguais;
Isósceles: Dois lados iguais;
Escaleno: Todos os lados diferentes.'''

reta1 = float(input('Informe o valor da primeira reta: '))
reta2 = float(input('Informe o valore da segunda reta; '))
reta3 = float(input('Informe o valor da terceira reta: '))

if reta1 == reta2 and reta2 == reta3:
    print(f'Os segmentos formam um triângulo equilátero.')
if reta1 != reta2 and reta2 != reta3 and reta3 == reta1:
    print('Os segmentos formam um triângulo Escalno')
else:
    print('Os segmentos formam um triângulo Isósceles')
#REVISAR CODIGO