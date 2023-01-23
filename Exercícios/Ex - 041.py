
('''A confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

Até 9 anos: MIRIM;
Até 14 anos: INFANTIL;
Até 19 anos: JÚNIOR;
Até 20 anos: SÊNIOR
Acima: MASTER.''')

from datetime import date
print('''Categoria de acordo com a idade
    Até 9 anos: MIRIM;
    Até 14 anos: INFANTIL;
    Até 19 anos: JÚNIOR;
    Até 20 anos: SÊNIOR
    Acima: MASTER.''')

nas = int(input('Informe o seu ano de nascimento: '))
atual = date.today().year - nas
if atual <= 9:
    print(f'Você tem {atual} anos e ainda está na categora Mirim')
elif atual > 9 and atual<= 14:
    print(f'Você tem {atual} e está na categoria iNFANTIL.')
elif atual >14 and atual <=19:
    print(f'Você tem {atual} e está na categoria JÚNIOR.')
elif atual >19 and atual <=20:
    print(f'Você tem {atual} e está na categoria SÊNIOR.')
else:
    print(f'Você tem {atual} e está na categoria MASTER.')