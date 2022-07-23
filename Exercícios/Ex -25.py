#Crie um programa que leia o nome de uma pessoa e diga se ela tem “Silva” nonome.

name = str(input('Informe o seu nome completo: ')).strip()
print(f'Seu nome completo tem silva?\n {"SILVA" in name.upper().split()}')