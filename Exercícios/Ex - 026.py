'''– Faça um programa que leia uma frase pelo teclado e mostre:
•
•
•
Quantas vezes aparece a letra “A”;
Em que posição ela aparece a primeira vez;
Em que posição ela aparece a última vez.'''

frase = str(input('Escreva uma frase qualquer:')).upper().strip()
print('')
print(f'A letra "A" aparece {frase.count("A")} vezes na frase {frase}')
print(f'Ela aparece pela primeira vez na {frase.find("A") +1}° posição\ne aparece pela última vez na {frase.rfind("A")+1}° posição.')

