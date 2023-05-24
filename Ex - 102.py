'''Crie um programa que tenha função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(num, show = False):
    """
    -Calcula o fatorial de um número
    : parametro n: O número a ser calculado
    : parametro show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range (num, 0,-1): #range do número até o zero voltando 1 (5 x 4 x 3 x 2 x 1)
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f

print(fatorial(5, show=False))
#print(help(fatorial))

