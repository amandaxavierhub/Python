''' Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha.'''

# l = linha. c = coluna


aux = [[0,0,0],[0,0,0],[0,0,0]]
soma  = 0
# inserindo os valores nas linhas e colunhas correspondentes
for l in range(0,3):    # passando pelas linhas
    for c in range(0,3):    # passando pelas colunas
        aux[l][c] = int(input(f'Informe o valor °{l} linha da °{c} coluna:  '))
     
for c in aux:
    for v in c:
        if v % 2 == 0:
            soma += v

# pegando o maior valor da segunda linha
maior = max(aux[1])
   
# somando todos os valores da terceira coluna
coluna = aux[0][2] + aux[1][2] + aux[2][2]
# descorrendo pela matriz para encontrar os valores par
#  
print(f'A soma de todos os números pares é de {soma}')
print(f'A soma dos valores da terceira coluna é igual a  {coluna} ')
print(f'O maior valor da segunda linha é {maior}')