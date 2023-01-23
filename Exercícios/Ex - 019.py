'''Um professor quer sortear um dos alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

for c in range (1,5):
    aluno = str(input('Informe o nome', c,  'do aluno: ')).strip()
    lista1 = [c - 1]
    escolha1 = random.choice(lista1)
print(escolha1)'''

# Outra alternativa

import random


n1 = str(input('Informe o nome do 1° aluno: '))

lista = [n1,n2, n3, n4]
escolha = random.choice(lista)

print(f'O aluno escolhido foi {escolha}')
