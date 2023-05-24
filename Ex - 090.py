'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
Acime de 7 "Aprovado".
Abaixo de 7 e acime de 5 "Em recuperação".
Abaixo de 5 "Reprovado". '''

aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Média do aluno: '))

if aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
elif 5 <=aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f'    * {k} é igual a {v}')
