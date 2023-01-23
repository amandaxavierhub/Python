# Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos
#dígitos separados.
from unicodedata import decimal


num = int(input('Informe um número entre 0 e 999:'))
unidade = num // 1 % 10
dezena = num // 10 %10
c = num // 100 % 10
m = num // 1000 % 10
print(f' Unidade {unidade}\n Dezena {dezena}\n c {c}\n m {m} ')