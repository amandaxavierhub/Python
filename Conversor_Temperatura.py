#Para converter celsius para fahrenheit multiplique a temperatura por 9, divida por 5 e some 32

celsius = float(input('Informe a da temperatura em graus celsius: '))
fah = ((celsius * 9)/5) + 32
print(f' a temperatura de {celsius}° em fahrenheit é de {fah}')

# Outra maneira seria multiplicar a temperatura por 1.8 e somar 32

c = float(input('Informe a temperatura em celsius:'))
f = (c * 1.8) + 32
print(f'A temperatura de {c}° em fahrenheit é de {f:.1f}')

#converter de fahr para celsius subtraia 32 e divida por 1,8

fahr = float(input('Digite a temperatura em fahrenheit: '))
cel: float = (fahr - 32)/1.8
print(f'a temperatura de fahrenheit para celsius é de {cel:.2f}°')

# Outra maneira seria subtrair fahrenheit por 32 multplicar por 9 e dividir por 5
FAR = float(input('temperatura em fahrenheit:'))
CEL = (FAR - 32)* 5
TO = CEL / 9
print(f'A temperatura de {FAR} em graus celsius é de {TO:.2f}°')
