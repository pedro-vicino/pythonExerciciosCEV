"""Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando  uma mensagem no final, de acordo com a média atingida:
-média abaixo de 5.0: reprovado
-média entre 5.0 e 6.9: recuperação
-média 7.0 ou superior: aprovado"""


nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5.0 :
    print(f"Sua nota foi {media}. Você está reprovado.")
elif media >= 5.0 and media < 7.0 :
    print(f"Sua nota foi {media}. Você ficou de recuperação!")
else :
    print(f"Parabéns! Sua nota foi {media} e você está aprovado!")