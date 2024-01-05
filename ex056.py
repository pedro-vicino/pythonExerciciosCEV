"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
-a media de idade do grupo
-qual é o nome do homem mais velho
-quantas mulheres tem menos de 20 anos"""
acumedia = 0
mediacalc = 0
maisvelhoidade = 0
maisvelhonome = ""
mulhermenos20 = 0
for pessoas in range(1, 5) :
    nome = str(input("Digite seu nome: ")).title()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo (M/F): ")).title()
    acumedia += idade
    mediacalc = acumedia / 4
    if pessoas == 1 and sexo in "M":
        maisvelhoidade = idade
        maisvelhonome = nome
    else:
        if idade > maisvelhoidade and sexo in "M":
            maisvelhoidade = idade
            maisvelhonome = nome
    if idade < 20 and sexo in "F" :
        mulhermenos20 += 1
print(f"A media da idade entre as pessoas citadas é de {mediacalc} anos")
print(f"O homem mais velha é o {maisvelhonome}, que possui {maisvelhoidade} anos")
if mulhermenos20 > 1 :
    print(f"Há no total {mulhermenos20} mulheres com menos de 20 anos")
else :
    print(f"Há no total {mulhermenos20} mulher com menos de 20 anos")