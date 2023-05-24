'''Um professor quer sortear um dos alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido'''

import random
for c in range (1,5):
    aluno = str(input(f'Informe o nome do {c}° aluno: ')).strip()
    lista1 = [c - 1]
    escolha1 = random.choice(lista1)
print(escolha1)
