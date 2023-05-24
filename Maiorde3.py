#exercício para saber quem é o maior e o menor número de 3

a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro núnmero: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor valor digitado foi {menor}')
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior valor digitado foi {maior}')