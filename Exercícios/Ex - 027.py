''''Faça um programa que leia o nome de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente. Ex : “Ana Maria de Souza”, primeiro = “Ana”
último = “Souza”'''

name = str(input('Escreva o sue nome completo: '))
separar = name.split()
print(f'Seu primeiro nome é {separar[0]} e o último é {separar[-1]}')
