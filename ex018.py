# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo
import math
angulo = float(input("Digite o ângulo: "))
numRad = math.radians(angulo)
sen = math.sin(numRad)
cos = math.cos(numRad)
tan = math.tan(numRad)

print(f"O seno desse ângulo é {sen:.2f} \nO cosseno desse ângulo é {cos:.2f} \nA tangente desse ângulo é {tan:.2f}")