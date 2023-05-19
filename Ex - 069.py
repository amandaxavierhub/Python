'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos;
B) Quantos homens foram cadastrados;
C) Quantas mulheres tem menos de 20 anos.
'''
contI = contM = contF  = 0
'''resposta = ""'''
while True:
    idade = int(input('Informe a sua idade: ')) 
    sexo = str(input('Informe o seu sexo: [M/F] '))
    if idade >= 18:
        contI += 1
    if sexo in "Mm":
        contM += 1
    if sexo in "Ff" and idade < 20:
        contF += 1
    resposta = str(input('Quer continuar: [S/N] ')).strip().upper()
    if resposta in 'Nn':
        break
print(f'''
{contI} pessoas tem mais de 18 anos.')
{contM} do sexo masculino foram cadastradas.
{contF} mulheres tem menos de 20 anos''')