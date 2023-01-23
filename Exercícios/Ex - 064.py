'''Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag 999).'''


soma = 0
c = 0
n = 1
print('Código de parada = 999')
while n != 999:
    n = int(input('Digite um valor: '))
    print(f' você digitou o número {n}')
    c += 1
    soma += n
print(f'Você teve um total de {c} tentativas e a soma de todos os valores digitados é de {soma - 999}.')
