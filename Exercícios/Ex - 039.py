'''– Faça um programa que leia o ano de nascimento de um jovem e informe, de
acordo com a sua idade:
•
•
•
Se ele ainda vai se alistar ao serviço militar;
Se é hora de se alistar;
Se já passou do tempo de alistamento.'''

from datetime import date

nascimento = int(input('IInforme o seu ano de nascimento: '))
idade = date.today().year - nascimento
prazo = idade + 18
if idade <= 17:
    print('Ainda não é hora de se alistar.')
    print(f'Você ainda tem {idade} anos e falta {18 - idade } anos para seu alistamento.')
elif idade >= 18 and idade <= 45:
    print('Está na hora de se alistar.')
else:
    print('Você passou da idade de 45 anos e não poderá se alistar.')
    print(f'Você deveria ter se alistado há {idade - 18} anos')