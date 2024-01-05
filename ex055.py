"""Faça um programa que leia o peso de 5 pessoas.
No final, mostre qual foi maior e menor peso lidos"""
maior = 0
menor = 0
pessoa = 1
for x in range(1, 6) :
    peso = float(input(f"Qual o peso da {pessoa} pessoa?: "))
    pessoa += 1
    if x == 1 :
        maior = peso
        menor = peso
    else :
        if peso > maior :
            maior = peso
        if peso < menor :
            menor = peso
print(f"O maior peso foi de {maior}kg")
print(f"O menor peso foi de {menor}kg")