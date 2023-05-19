'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor
do seu aumento. Para salários superiores a R$1.250, calcule um aumento de 10%. Para
os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Informe o seu salário: '))
if salario > 1250:
    print(f'O seu salário com acrescimo de 10% é de {((salario * 10)/100) + salario}')
else:
    print(f'O seu salário com acrescimo de 15% é de {((salario * 15)/100) + salario}')
