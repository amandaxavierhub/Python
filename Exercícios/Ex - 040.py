'''Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem final, de acordo com a média atingida:
•
•
Média abaixo de 5.0: REPROVADO;
Média entre 5.0 e 6.9: RECUPERAÇÃO;•
Média 7.0 ou superior: APROVADO.'''

nota1 = float(input('Informe a 1º nota '))
nota2 = float(input('Informe a 2º nota: '))
media = (nota1 + nota2)/ 2
if media >= 7:
    print('APROVADO!')
elif media < 5:
    print('REPROVADO')
else:
    print('RECUPERAÇÃO!')