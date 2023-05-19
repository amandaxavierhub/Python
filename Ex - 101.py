'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''

def voto(ano):
  from datetime import date
  atual = date.today().year
  idade = atual - ano
  if idade <16:
    return f'Com {idade} anos o voto é negado.'
  elif 16 <= idade <18 or idade >65:
    return f'Com {idade} anos o voto é opcional.'
  else:
    return f'Com {idade} anos o voto é obrigatório.'

nas = int(input('Informe o seu nao de nascimento: '))
print(voto(nas))