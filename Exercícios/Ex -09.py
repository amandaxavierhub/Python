# showe multiplication table

num = int(input('Digite um número inteiro e veja a sua tabuada: '))
print('\033[1;31m=\033[m'*12)
print('\033[4;34m{} x {:2} = {} '.format(num, 1, num * 1))
print('{} x {:2} = {} '.format(num, 2, num * 2))
print('{} x {:2} = {} '.format(num, 3, num * 3))
print('{} x {:2} = {} '.format(num, 4, num * 4))
print('{} x {:2} = {} '.format(num, 5, num * 5))
print('{} x {:2} = {} '.format(num, 6, num * 6))
print('{} x {:2} = {} '.format(num, 7, num * 7))
print('{} x {:2} = {} '.format(num, 8, num * 8))
print('{} x {:2} = {} '.format(num, 9, num * 9))
print('{} x {:2} = {}\033[m '.format(num, 10, num * 10))
print('\033[1;31m=\033[m'*12)

