'''Desenvolva uma lógica que leia o peso de uma pessoa, calcule seu imc e mostre
seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do peso;
Entre 18.5 e 25: Peso ideal;
25 até 30: Sobrepeso;
30 até 40: Obesidade;
Acima de 40: Obesidade mórbida.'''

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / altura
if imc < 18.5:
    print('Abaixo do peso.')
if imc >= 18.5 and imc < 25:
    print('Peso Ideal')
if imc >= 25 and imc <=30:
    print('Sobrtpeso.')
if imc >=30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
