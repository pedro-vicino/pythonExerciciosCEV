"""Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome"""

nomePessoa = str(input("Digite o seu nome: ")).upper()
if "SILVA" in nomePessoa :
    print("Seu nome possui Silva!")
else :
    print("Seu nome NÃO possui Silva!")