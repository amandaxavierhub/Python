''' Crie um programa que  vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
contador = 0
while True:
    num = int(input('Informe um valor qualquer: '))
    lista.append(num)
    lista.sort(reverse=True)
    res = str(input('Gostaria de tentar mais uma vez? [S/N]')).upper().strip()
    if res != 'S' and res != 'N':
        print('Opção inválida. Tente novamente.')
        res = str(input('Gostaria de tentar mais uma vez? [S/N]')).upper().strip()
    elif res in "Nn":
            break
    if 5 in lista:
        contador += 1
    else:
        pass

print(f'Ao todo foram digitados {len(lista)} valores.')   
print(f'Os número digitados em ordem decrescente {lista}')
if contador >=1:
    if contador >1:
        print(f'O número 5 foi digitado {contador} vezes.')
    else:
        print(f'O número 5 foi digitado {contador} vez.')   
else:
    print('O número 5 não foi digitado.')