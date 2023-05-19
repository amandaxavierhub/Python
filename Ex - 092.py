'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferene de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Para se aposentar considerar 35 anos de contribuição.'''

from datetime import date

cadastro = {}

cadastro['nome'] = str(input('Informe o nome completo: '))
nasc = int(input('Informe o ano de nascimento: '))
cadastro['idade'] = date.today().year - nasc
cadastro['ctps'] = int(input('Informe o número da Carteira de Trabalho [digite 0 caso não tenha]: '))

if cadastro['ctps'] == 0:
    for k, v in cadastro.items():
        print(f'    {k} tem o valor de {v}')
else:
    cadastro['contrato'] = int(input('  Informe o ano de contratação: ')) 
    cadastro['salario'] = float(input('  Informe o salário: '))
    cadastro['aposentadoria'] = ( cadastro['contrato'] - nasc) + 35

    for k, v in cadastro.items():
        print(f'    * {k} tem o valor de: {v}')

