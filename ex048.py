#Faça um programa que calcule a soma entre todos os números ímpares que 
#são múltiplos de três e que se encontram no intervalo de 1 até 500
acu = 0
contador = 0
for num in range(1, 501, 2) :
    if num % 3 == 0 :
        acu += num
        contador += 1
print(f"Foram contados {contador} números e a soma entre ele será {acu}")