"""escreva um programa que leia a velocidade de um carro.
se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
a multa vai custar R$7.00 por cada km acima do limite"""

velocidade = float(input("Qual a velocidade do carro?: "))
multa = (velocidade - 80) * 7
if velocidade > 80 :
    print(f"Você foi multado por exceder a velocidade! \nSua multa será de R${multa}")
else :
    print("A velocidade não ultrapassa o limite!")