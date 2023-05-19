'''Faça um programa que tenha uma função notas() que pode receber várias notas dos alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma;
- A situação (opcional).
Adicione também as docstrings da função.
'''

def notas(*n, sit=False):
    """
    - Análisa a situação do aluno de acordo com a média.
     :parâmentro n: aceita uma ou mais notas do aluno.
     :parâmetro sit: é um valor opcional e indica qual a situação atual do aluno.
     return: retorna o dicionário que contém várias informações sobre as notas do aluno.
    """
    r = dict()
    r['Total'] =  len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r
print('')
res = notas(10, 4, 6, sit=True)
print(res)
print('')
#help(notas)