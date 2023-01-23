''' Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

alunos = []
cont = 0
while True:
    nome = str(input('Informe o nome do aluno: '))
    nota1 = float(input(f'Informe a 1° nota de {nome} '))
    nota2 = float(input(f'Informe a 2° nota de {nome} '))
    media = (nota1 + nota2)/2
    alunos.append([nome, [nota1, nota2], media])
    res = str(input('Gostaria de cadastrar mais um aluno? [S/N] ')).strip().upper()
    if res in 'Nn':
        break
print()
for c in alunos:
    print(f'N° {cont} |Aluno(a) = {c[0]} |Média = {c[2]}')
    print('-' *60)
    cont+=1
while True:
    res2 = int(input('[1] Nota aluno: N° \n[2] Finalizar programa:\n '))
    if res2 == 1:
        escolha = int(input('Escolha o número correspondente ao aluno: '))
        print()
        print(f'{alunos[escolha][0]}| Nota {alunos[escolha][1]}')
        print()
    elif res2 ==2:
        break
print()
print('* Programa Finalizado *'.center(60))
print('=' *60)