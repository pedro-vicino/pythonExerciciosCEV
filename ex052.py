"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo"""
total = 0
num = int(input("Digite um número: "))
for x in range(1, num + 1) :
    if num % x == 0 :
        print('\033[34m', end=" ")
        total += 1
    else :
        print('\033[35m', end=" ")
    print(x, end=" ")
if total == 2 :
    print(f"\n\033[mO número {num} foi divisível {total} vezes, portanto ele é PRIMO")
else :
    print(f"\n\033[mO número {num} foi divisível {total} vezes, portanto ele NÃO é primo")
