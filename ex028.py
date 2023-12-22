# Escreva um programa que faça o computador "pensar" 
# em um número inteiro entre 1 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador
# o programador deverá escrever na tela se o usuário venceu ou perdeu

import math, random

usuario = int(input("Tente adivinhar o número entre 1 e 5: "))
num = random.randint(1, 5)
if(num == usuario) :
    print(f"Você venceu! O número sorteado foi {num}")
else :
    print(f"Você perdeu... O número sorteado, na verdade, foi o {num}")
