# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# US$1.00 = R$3.27

valor = float(input("Quanto dinheiro você possui? "))
dolar = valor / 3.27
print(f"Você pode comprar {dolar:.2f} dólares")
