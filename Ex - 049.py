'''Faça o desafio 09, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

n = int(input('Enter a value and find your multiplication table:'))
print('')
for c in range (1,12 -1):
    t = c * n
    print(f'{n} x {c} = {t}')

    