"""Desenvolva uma lógica  que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-abaixo de 18.5: abaixo do peso
-entre 18.5 e 25: peso ideal
-25 até 30: sobrepeso
-30 até 40: obesidade
-acima de 40: obesidade mórbida"""

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura ** 2)
if imc < 18.5 :
    print(f"Seu IMC é {imc}. Você está abaixo do peso!")
elif 18.5 <= imc < 25 :
    print(f"Seu IMC é {imc}. Você está no peso ideal!")
elif 25 <= imc < 30 :
    print(f"Seu IMC é {imc}. Você está em sobrepeso!")
elif 30 <= imc < 40 :
    print(f"Seu IMC é {imc}. Você está obeso!")
else : 
    print(f"Seu IMC é {imc}. Você está em obesidade mórbida!")
    