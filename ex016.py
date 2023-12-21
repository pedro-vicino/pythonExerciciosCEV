# Crie um programa que leia um número real qualquer e mostre na tela sua porção inteira
import math
num = float(input("Digite um número real: "))
numTrunc = math.trunc(num)
print(f"O número {num}, na sua forma inteira, será {numTrunc}")