"""crie um programa que leia uma frase qualquer e diga se
ela é um palíndromo, desconsiderando os espaços"""

usuario = str(input("Digite uma frase: ")).strip().upper()
palavra = usuario.split()
juntar = "".join(palavra)
inverso = ""

for letra in range(len(juntar) -1, -1, -1) :
    inverso += juntar[letra]
if inverso == juntar :
    print(f"{juntar} invertido ficará {inverso}")
    print("A frase digitada é um PALÍNDROMO")
else :
    print(f"{juntar} invertido ficará {inverso}")
    print("A frase digitada NÃO é m palíndromo")