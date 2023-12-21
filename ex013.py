# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salário = float(input("Digite seu salário: "))
reajuste = salário + (salário * 15/100)
print(f"Seu salário de R${salário}, com um aumento de 15%, passára a ser R${reajuste}")