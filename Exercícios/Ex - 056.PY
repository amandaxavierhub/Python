''''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do
programa mostre:
A média de idade do grupo;
Qual é o nome do homem mais velho;
Quantas mulheres têm menos de 20 anos;'''

from mailbox import NotEmptyError


somaidade = 0
mediaidade = 0
maiorIdade = 0
oldman = ''
totMulher = 0
for t in range (1,5):
    name = str(input('Informe o seu nome: '))
    idade = int(input('Quantos anos você tem? '))
    sexo = str(input('Qual o seu sexo? [F/M]'))

    somaidade += idade
    if t == 1 and sexo in "Mm":
        maiorIdade = idade
        oldman = name
    if sexo in "Mm" and idade > maiorIdade:
        maiorIdade = idade
        oldman = name
    if sexo in "Ff" and idade < 20:
        totMulher +=1

mediaidade = somaidade/14

print(f'''A média de idade do grupo é {mediaidade}
          O homem mais velho tem {maiorIdade} anos e se chama {oldman}
          Ao todo são/é {totMulher} mulher/mulheres com menos de 20 anos  ''')