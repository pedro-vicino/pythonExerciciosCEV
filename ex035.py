"""Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar um triângulo"""

""""se a soma das medidas de dois deles é sempre maior
que a medida do terceiro, então, eles podem formar um triângulo."""

c1 = float(input("Digite o primeiro comprimento: "))
c2 = float(input("Digite o segundo comprimento: "))
c3 = float(input("Digite o terceiro comprimento: "))
if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1 :
    print("Com essas medidas, é possível formar um triângulo!")
else :
    print("Com essas medidas, NÃO é possível formar um triângulo!")
