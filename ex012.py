# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preço = float(input("Digite o preço do produto: "))
desconto = preço - (preço * 5/100)
print(f"Seu produto, que antes valia R${preço}, agora vale R${desconto}, com o desconto de 5%!")