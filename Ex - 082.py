''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final mostre o conteúdo das três listas gerados.'''

lista = []
listapar = []
listaimpar = []

while True:
    num = int(input('Informe um valor: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    res = str(input('Gostaria de cadastrar mais um número? [S/N]')).upper().strip()
    if res in "Nn":
        break

print(f'  Os números cadastrados foram {lista}\n Os números pares cadastrados foram {sorted(listapar)} \n Os números ímpares cadastrados foram {sorted(listaimpar)}.')