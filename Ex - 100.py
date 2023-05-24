''' Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteios () e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.'''

from random import randint

# Definindo cores
cor_verde = "\033[92m"
cor_roxo = "\033[94m"
cor_reset = "\033[0m"

def sorteios():
    numeros = []
    for c in range(0,5):
        num = randint(0,10)
        numeros.append(num)
    def somaPar():
        soma = 0
        for c in numeros:
            if c % 2 == 0:
                soma += c
        return soma
    print(cor_roxo + f'Os números sortedos foram {numeros}' + cor_reset)
    print(cor_verde + "Soma dos números pares:" + cor_reset, somaPar() )


sorteios()