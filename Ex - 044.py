'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
À vista dinheiro/cheque: 10% de desconto;
À vista no cartão: 5% de desconto;
Em até 2x no cartão: Preço normal;
3x ou mais no cartão: 20% de juros.'''

valor = float(input('Informe o valor do produto: '))
print('''Escoha a forma de pagamento
1 - À vista dinheiro/cheque: 10% de desconto;
2 - À vista no cartão: 5% de desconto;
3 - Em até 2x no cartão: Preço normal;
4 - 3x ou mais no cartão: 20% de juros;
5 - Sair do programa''')
escolha = int(input('Informe a sua escolha: '))
if escolha ==1 :
    print(f'O valor a ser pago com 10% de desconto é de R${valor - (valor * 10)/100 }')
if escolha ==2 :
    print(f'O valor a ser pago com 5% de desconto é de R${ valor- (valor *5)/100}')
if escolha == 3:
    print(f'O valor a ser pago será de R${valor} sem desconto.')
if escolha == 4:
    print(f'O valor a ser pago com 20% de juros será de R${(valor * 20)/100 + valor}')
if escolha == 5:
    print('Obrigado pela sua participação.')
    quit()
elif escolha > 5:
    print('Opção inválida.')
    