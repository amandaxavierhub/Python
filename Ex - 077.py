''' Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar para cada palavra quais são as suas vogais.'''

tupla = ('Primeiro', 'Segundo', 'Terceiro')

#varrendo a tupla
for c in tupla:
    print(f'\nNa palavra {c.upper()} temos as vogais ', end ='')
    #varrendo cada item da tupla
    for l in c:
        if l.lower() in 'aeiou':
            print(l, end= ' ')