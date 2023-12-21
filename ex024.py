"""Crie um programa que leia o nome
de uma cidade e diga se ela começa ou não com a palavra Santo"""

nomeCidade = str(input("Digite o nome da cidade: ")).upper()
nomeSplit = nomeCidade.split()
if "SANTO" in nomeSplit[0] :
    print("Sua cidade começa com Santo!")
else :
    print("Sua cidade NÃO começa com Santo")