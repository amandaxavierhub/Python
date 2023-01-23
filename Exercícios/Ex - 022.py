'''Crie um programa que leia o nome completo de uma pessoa e mostre:
•
•
•
•
O nome com todas as letras maiúsculas.
O nome com todas as letras minúsculas.
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome.'''

name = str(input('Escreva o seu nome completo: ')).strip()
print(f' Seu nome completo em letras Maiúsculas é: {name.upper()}\n Seu nome completo em letras minúsculas é: {name.lower()}')
separa = name.split()
print(f' Ao todo seu nome possui: {len(name) - name.count(" ")} letras.\n Seu primeiro nome tem {name.find(" ")} letras e ele é {separa [0]}')
# nota: usa-se aspas duplas dentro dos parenteses
