'''O mesmo professor do desafio anterior que sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a
ordem sorteada.'''

import random

n1 = str(input('Informe o nome do 1° aluno: '))
n2 = str(input('Informe o nome do 2° aluno: '))
n3 = str(input('Informe o nome do 3° aluno: '))
n4 = str(input('Informe o nome do 4° aluno: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem de apresentação será: {lista} \n')