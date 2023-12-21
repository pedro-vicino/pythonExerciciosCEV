# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input("Digite um valor em metros: "))
centimetro = valor * 100
milimetro = valor * 1000
print(f"O valor de {valor}m, em centímetros é de {centimetro}cm, e em milímetros é de {milimetro}mm")