''' Crie um programa que  vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista =[]
while True:
    num  = int(input('Digite um valor: '))
    if num >= 0:
        lista.insert(num)
    else:
        for pos, c in enumerate(lista):
            pos = 0
            if num >= c:
                lista.insert(pos, num)
                break
            pos +=1
    res = str(input('Gostaria de tentar mais uma vez? [S/N]')).upper().strip()
    if res != 'S' and res != 'N':
        print('Opção inválida. Tente novamente.')
        res = str(input('Gostaria de tentar mais uma vez? [S/N]')).upper().strip()
    elif res in "Nn":
            break
print(lista)