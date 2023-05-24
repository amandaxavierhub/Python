''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro ele não será adicionado. No final serão exibidos todos os valores
  únicos digitados em ordem crescente. 
'''
res = 'S'
cadastro =[]
while res in 'S':
    numero = (int(input('Digite um valor qualquer: ')))
    if numero not in cadastro:
           cadastro.append(numero)
    else:
        print("Valor já foi cadastrado!")
    res = str(input('Gostaria de tentar mais uma vez? [S/N]')).upper().strip()
    if res != 'S' and res != 'N':
        print('Opção inválida. Tente novamente.')
        res = str(input('Gostaria de tentar mais uma vez? [S/N]')).upper().strip()
    elif res in "Nn":
            print('Finalizando programa.')
print(f"Os números cadastrados em ordem crescente foram {sorted(cadastro)}")