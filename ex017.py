# Faça um programa que leia o comprimento do cateto adjacente e oposto de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa
import math
catO = float(input("Digite a medida do cateto oposto: "))
catA = float(input("Digite a medida do cateto adjacente: "))
hipotenusa = math.sqrt(math.pow(catO, 2) + math.pow(catA, 2))
print(f"A hipotenusa será {hipotenusa} \nCateto oposto: {catO} \nCateto adjacente: {catA}")