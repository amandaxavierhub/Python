'''Faça um minisistema que utilize o interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
OBS: Use cores'''

from time import sleep

color = {'clear': '\033[m', 'green': '\033[1;42m', 'blue': '\033[1;44m', 'white': '\033[1;30;107m', 'red': '\033[1;41m'}

def tit(msg, cor='clear'):
    """
    → funcao que trata uma string passada pelo parametro.
    :param msg: string passada no parâmetro para tratamento.
    :param cor: usado em conjunto com o dicionario 'color'. defaut:clear.
    :return: Essa função não retorna valores.

    """
    t = len(msg) + 4
    print(f'{color[cor]}', end='')
    print('~'*t)
    print(f'{msg:^{t}}')
    print('~'*t)
    print(f'{color["clear"]}', end='')

def pyhelp(comand, cor='clear'):
    """
    → Função que utiliza o Interactive Help do Python.
    :param comand: usuário digita qual comando deseja ver o manual.
    :param cor: usado em conjunto com o dicionario 'color'. defaut:clear.
    :return: Comando 'help' não retorna valor, então está função não retorna nada.

    """
    tit(f'Acessando o manual do comando \'{comand}\'', cor='blue')
    sleep(1)
    print(f'{color[cor]}')
    help(comand)
    print(f'{color["clear"]}', end='')
    sleep(2)

while True:

    tit('SISTEMA DE AJUDA PyHELP', cor='green')
    func = input('Função ou Biblioteca > ')
    if func.upper() in 'FIM':
        tit('ATÉ LOGO!', 'red')
        break
    pyhelp(func, cor='white')


