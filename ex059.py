"""crie um programa que leia dois valores e mostre um menu. 
Seu programa deverá realizar a operação solicitada em cada caso
(somar, multiplicar, maior, novos números, sair do programa)"""


soma = 0
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
opcoes = 0
while opcoes != 5:
    opcoes = int(input("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Digite qual opção você deseja: """))
    if opcoes == 1 :
        soma = num1 + num2
        print(f"\033[34m{num1} + {num2} = {soma}\033[m")
    elif opcoes == 2:
        mult = num1 * num2
        print(f"\033[34m{num1} x {num2} = {mult}\033[m")
    elif opcoes == 3 :
        if num1 > num2 :
            print(f"\033[34mO número {num1} é maior que o número {num2}\033[m")
        elif num1 < num2 :
            print(f"\033[34mO número {num2} é maior que o número {num1}\033[m")
        else :
            print("\033[34mOs números são iguais!\033[m")
    elif opcoes == 4 :
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))
    print("+=" * 14)

print("Fim do programa!")