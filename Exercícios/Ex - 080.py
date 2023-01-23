'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort(). No final, mostre a lista ordenada na tela.'''

lista = []

for contador in range(0,5):
    numero = int(input('Digite um valor inteiro: '))
    if contador == 0:
        lista.append(numero) # número adicionado no final da lista
    elif numero > lista[-1]: #se o novo número adicionado for maior que o último número da lista
        lista.append(numero) # novo número adicionado no final da lista
    else:
        pos = 0 #definindo o inicio da posição da lista 
        for pos, contador in enumerate(lista): #iniciando o contador em cada posiçao da lista
            if numero <= contador: #se o numero for menor que o valor do contador
                lista.insert(pos, numero) # a lista recebe o numero na posicao do contador
                break
           

print(f'Os números digitados em ordem são {lista}.')