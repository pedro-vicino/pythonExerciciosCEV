# Escreva um programa que pergunte a quantidade de Km percorridos
#  por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado

percorreu = int(input("Digite quantos quilometros você percorreu com o carro alugado: "))
dias = int(input("Digite por quantos dias você alugou o carro: "))
preçoAluguel = dias * 60
preçoKm = percorreu * 0.15
total = preçoAluguel + preçoKm
print(f"O total a ser pago é R${total}.\nO preço total do aluguel é de R${preçoAluguel}, e o preço total por Km andado é R${preçoKm}")