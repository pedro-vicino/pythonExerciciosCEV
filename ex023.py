"""Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos seus dígitos separados
ex: 1839
unidade: 9
dezena: 3
centena: 8
milhar: 1"""

num = str(input("Digite um número de 0 a 9999: "))
print(f"Unidade: {num[3]} \nDezena: {num[2]} \nCentena: {num[1]} \nMilhar: {num[0]}")