#Refaça o desafio 009, mostrando a tabuada de um 
#número que o usuário escolher, só que agora utilizando um laço for"""

num = int(input("Digite um número para descobrir sua tabuada: "))
limite = int(input("Digite até que número a tabuada fará as multiplicações: "))
for f in range(1, limite+1) :
    print(num, "x", f, "=", num*f)