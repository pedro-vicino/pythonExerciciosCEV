"""Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem,
cobrando R$0.50 por Km para viagens de 
até 200Km e R$0.45 para viagens mais longas"""

distancia = float(input("Qual a distância da viagem?: "))
if distancia <= 200 :
    preço = distancia * 0.50
    print(f"O preço da passagem será de R${preço}")
else :
    preço = distancia * 0.45
    print(f"O preço da passagem será de R${preço}")
