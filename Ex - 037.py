'''– Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual a base de conversão.
•
•
•
1 – Para binário;
2 – Para octal;
3 – Para hexadecimal.'''

import math

    
print('=-=-= Conversor =-=-=')
num = int(input('Informe um número inteiro: '))
print('''Escolha para converter:
    =-=-=-=-=-=-=-=-=-=-=--=-=-=-=-= 
        1 - Para binário:
        2 - Ṕara Octal:
        3 - Para Hexadecimal:
        4 - Para sair do programa''')
escolha = int(input('Informe a sua escolha: '))

if escolha == 1:
        print(f'O número {num} em binário é {bin(num)}')
if escolha == 2:
        print(f'O número {num} convertido para octal é {oct(num)}.')
if escolha == 3:
        print(f'O número {num} convertido em hexadecimal é {hex(num)}.')
if escolha == 4:
        print(f'Obrigado pela sua participação.')
        quit()
elif escolha > 4:
        print('Opção Inválida')
   
    
