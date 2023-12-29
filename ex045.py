"""crie um programa que faça o computador jogar jokenpô com você"""
import random

usuario = int(input("""Escolha uma das opções
[1] Pedra
[2] Papel
[3] Tesoura
Digite a opção escolhida: """))
print("+="*14)
computador = random.randint(1, 3)
if computador == 1 : #pedra
    if usuario == 1 :
        print("EMPATE!")
    elif usuario == 2 :
        print("Jogador GANHOU!")
    elif usuario == 3 :
        print("Computador GANHOU!")
    else :
        print("Opção inválida!")
elif computador == 2 : #papel
    if usuario == 1 :
        print("Computador GANHOU!")
    elif usuario == 2 :
        print("EMPATE!")
    elif usuario == 3 :
        print("Jogador GANHOU")
    else :
        print("Opção inválida!")
else : #tesoura
    if usuario == 1 :
        print("Jogador GANHOU")
    elif usuario == 2 :
        print("Computador GANHOU")
    elif usuario == 3 :
        print("EMPATE!")
    else :
        print("Opção inválida!")
print("-"*25)
print(f"Computador escolheu {computador}")
print(f"Usuário escolheu {usuario}")
print("-"*25)

# se quiser algo mais bonito, como "computador escolheu PEDRA, 
# basta colocar dentro do escopo"