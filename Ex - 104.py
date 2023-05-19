'''Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhanta à função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico.
Ex:
n = leiaint(‘Digite um número: ’) '''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('Valor inválido. Digite um número inteiro: ')
            continue
        else:
            return n

n = leiaInt('Digite um número inteiro qualquer: ')
print(f'O número digitado foi {n}')