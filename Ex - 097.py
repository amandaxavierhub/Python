''' Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escrever(msg):
    print()
    print('-'*len(msg))
    print(msg)
    print('-'* len(msg))


escrever(str(input('Escreva qualquer frase aqui: ')))