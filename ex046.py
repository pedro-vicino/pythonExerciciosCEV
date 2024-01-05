#faça um programa que mostre na tela uma contagem regressiva
#para o estouro de fogo de artifício, indo de 10 até 0, com uma pausa
# de 1 segundo entre elas

import time

for x in range(10, 0, -1) :
    print(x)
    time.sleep(1)
print("FELIZ ANO NOVO!")