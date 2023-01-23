'''– Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantas
vezes ele vai pagar. Calcule o valor da prestação mensal, sabendo que não pode
exceder 30% do salário ou então o empréstimo será negado.'''

from sys import float_repr_style


casa = float(input('Informe valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos = int(input('Informe a quantidade de parcelas: '))
parcela = casa / (anos * 12)
pagamento = (salario * 30 /100) + salario
if parcela <= pagamento:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo reprovado!')
