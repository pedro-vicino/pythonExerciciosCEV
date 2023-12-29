"""escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
-o primeiro valor é maior
-o segundo valor é maior
-não existe valor maior, os dois são iguais"""

num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva outro número: "))

if num1 > num2 :
    print(f"O primeiro valor ({num1}) é maior que o segundo ({num2})!")
elif num2 > num1 :
    print(f"O segundo valor ({num2}) é maior que o primeiro ({num1})!")
else:
    print("Os valores são iguais!")