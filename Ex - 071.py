''' Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Nota:  Considere que o caixa possui notas de R$ 50, R$20, R$10 e R$1.'''

cinquenta = vinte =  dez = um = inteiro =  0
n = int(input('Informe o valor do saque: '))

# resolvendo notas de 50
cinquenta =int((n / 50))
n = n - (cinquenta * 50)
inteiro = n 

    #resolvend0 notas de 20
vinte = int(inteiro / 20)
inteiro = inteiro - (vinte * 20)
inteirodez = inteiro

#resolvendo notas de 10
dez = int(inteirodez /10)
inteirodez = inteirodez - (dez * 10)
inteiroum = inteirodez

#resolvendo notas de 1
um = int(inteiroum / 1)
inteiroum = inteiroum - (um * 1)
umint = inteiroum
       
print(f'''
{cinquenta} cédulas de R$50,00
{vinte} cédulas de R$20,00
{dez} cédulas de R$10,00
{um} cédulas de R$1,00
''')
