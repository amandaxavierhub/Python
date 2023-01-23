'''Crie um programa que tenha uma tupla totalmente preenchida com um contagem por extenso de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numeros = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoisto', 'dezenove', 'vinte')
n = ''
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0<= num <=20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {numeros[num]}')
    n = str(input('Quer continuar?  [S/N]')).upper().strip()
    if n in "Nn":
        break


'''Nota: 
    O primeiro while se refere a questão S/N
    O segundo while está subordinado ao primeiro, este que se refere ao número digitado, isto é
    o segundo while só irá se repetir se o primeiro se tornar falso'''