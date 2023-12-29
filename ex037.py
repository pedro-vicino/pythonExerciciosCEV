"""escreva um programa que leia um número inteiro qualquer e converta e peça para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal"""

num = int(input("Digite um número: "))
escolher = int(input("""Escolha se ele será convertido para: 
[1] Binário
[2] Octal
[3] Hexadecimal \nDigite uma das opções: """))
if escolher == 1 :
    print(f"O número {num} convertido para binário fica {bin(num)}")
elif escolher == 2 :
    print(f"O número {num} convertido para octal fica {oct(num)}")
elif escolher == 3 :
    print(f"O número {num} convertido para binário fica {hex(num)}")
else :
    print(f"Houve um erro.")
