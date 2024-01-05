"""desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
daqueles que forem par. Se o valor digitado for ímpar, desconsidere-o"""
pares = 0
acu = 0
for x in range(1, 7) :
    n = int(input("Digite um número: "))
    if n % 2 == 0 :
        acu += n
        pares += 1
print(f"A soma entre os números PARES foi {acu} (foram digitados {pares} números pares)")
