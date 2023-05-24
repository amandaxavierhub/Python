'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou
‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = ''
while sexo != "F" and sexo != "M":
    sexo = str(input('Informe o seu sexo: [F/M]'))
    if sexo in "F" or sexo in "M":
        print('Dados registrado com sucesso! Obrigado por participar')
    else:
        print('Opção inválida!')
        quit()