''' Crie um programa que leia nome, sexo e idade de várias pessaos, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas os mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
'''
pessoas = []
dados = {}
media = soma =0
#criando o loop do código
while True:
    dados['nome'] = str(input('Nome: '))
    # validando a resposta do "sexo"
    while True: 
        dados['sexo'] = str(input('Sexo[F/M] ')).upper()[0]
        if dados['sexo'] in "MF":
            break
        else:
            print('Digite apenas F ou M.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    # validando a resposta "res"
    while True:
        res = str(input('Quer continuar [S/N]? ')).upper()[0]
        if res in "SN":
            break
        else:
            print('Digite apenas S ou N.')
    if res in "Nn":
        break
print(' ===== INFORMAÇÕES DE CADASTRO ====='.center(30))
print(f' => {len(pessoas)} pessoas foram cadastradas.')
media = soma/len(pessoas)
print(f' => A média da idade das pessoas é {media:5.2f} anos.')
print(f' => Lista com as mulheres cadastradas:')
for c in pessoas:
    if c['sexo'] in "F":
        print(f'    |{c["nome"]} ', end='')
print()
print(f' => Lista de pessoas com idade acima da média: ')
for c in pessoas:
    if c['idade'] > media:
        print(f'    |{c["nome"]} ', end='')
print()
print('='*30)