#programa tabuada

num = int(input('\033[1;34mDigite um número inteiro:\033[m '))
for c in range(1, 11):
    print('\033[1;35m{} X {:2} = {}\033[m'.format(num, c, num * c))

