'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar;
[2] Multiplicar;
[3] Maior
[4] Novos números;
[5] Sair do programa.
Seu programa deverá realizar a operação solicitada em cada caso.'''

maior = 0
print('Menu de valores')
print('=+'*12)

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
res = 0
while res != 5:    
    print('=+'* 12)
    print('''
        MENU
    [1] SOMAR;
    [2] MULTIPLICAR;
    [3] MAIOR;
    [4] NOVOS NÚMEROS;
    [5] SAIR DO PROGRAMA.
    ''')

    print('=+'* 12)
    res = int(input('Escolha uma opção: '))

    if res == 1:
     print('O resultado da soma entre os valores é >>')
     print(f'{valor1} + {valor2} = {valor1 + valor2}')

    elif res == 2:
        print('O resultado da multiplicação entre os valores é >>')
        print(f'{valor1} X {valor2} = {valor1 * valor2}')

    elif res == 3:
        maior = valor1
        if valor1 > valor2:
            maior = valor1
            print(f'O maior valor digitado foi {maior}')
        else:
            maior = valor2
            print(f'O maior valor digitado foi {maior}')
            
    elif res == 4:
        print('Digite os novos valores.')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
            
    else:
        print('Obrigado por participar!')
        quit()


