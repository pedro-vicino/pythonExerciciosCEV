"""faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'm' ou 'f'. 
Caso esteja errado, peça novamente até ter um valor correto"""
sexo = str(input("Digite seu sexo(M/F): ")).upper()
# while sexo not in "MF" :
#     sexo = str(input("Dado inválido. Tente novamente: "))
while sexo != "M" and sexo != "F" :
    sexo = str(input("Dado inválido. Tente novamente: "))
print(f"Sexo {sexo} registrado corretamente")