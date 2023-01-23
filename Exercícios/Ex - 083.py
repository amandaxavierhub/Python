'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

exp = []
total = []
exp = str(input('Digite um expressão'))
for parentese in exp:
    if parentese == '(':
        total.append('(')
    elif parentese == ')':
        if len(total) > 0:
            total.pop()
        else:
            total.append(')')
            break
if len(total) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
