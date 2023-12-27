"""Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento
Para salários superiores a R$1250.00, calcule um aumento de 10%
para os inferiores ou iguais, o aumento é de 15%"""

salario = float(input("Digite seu salário para ser reajustado: "))

if salario > 1250 :
    aumento = salario + (salario * 10/100)
    print(f"Seu novo saçario será de R${aumento}")
else :
    aumento = salario + (salario * 15/100)
    print(f"Seu novo saçario será de R${aumento}")