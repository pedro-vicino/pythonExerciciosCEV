"""Faça um programa que leia uma frase pelo teclado e mostre:
- quantas vezes aparece a letra "a"
- em que posição ela aparece a primeira vez
- em que posição ela aparece a última vez"""

frase = str(input("Digite uma frase qualquer: ")).lower().strip()
print('A letra "a" aparece {} vezes na frase!'.format(frase.count("a") + 1))
print('A letra "a" aparece pela primeira vez na {}° posição'.format(frase.find("a") + 1))
print('A letra "a" aparece pela última vez na {}° posição'.format(frase.rfind("a") + 1))