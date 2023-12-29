"""Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que
tipo de triângulo será formado:
-equilátero: todos os lados iguais
-isósceles: dois lados iguais
-escaleno: todos os lados diferentes"""

c1 = float(input("Digite o primeiro comprimento: "))
c2 = float(input("Digite o segundo comprimento: "))
c3 = float(input("Digite o terceiro comprimento: "))
if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1 :
    print("Com essas medidas, é possível formar um triângulo!")
    if c1 == c2 == c3 :
        print("Esse triângulo é EQUILÁTERO")
    elif c1 != c2 != c3 != c1 :
        print("Esse triângulo é ESCALENO")
    else :
        print("Esse triângulo é ISÓSCELES")
else :
    print("Com essas medidas, NÃO é possível formar um triângulo!")