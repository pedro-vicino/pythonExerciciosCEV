# Um professor quer sortear uma ordem de apresentação de trabalho dos seus alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
aluno1 = str(input("Digite o nome do primeiro aluno: "))
aluno2 = str(input("Digite o nome do segundo aluno: "))
aluno3 = str(input("Digite o nome do terceiro aluno: "))
aluno4 = str(input("Digite o nome do quarto aluno: "))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f"A ordem de apresentação será: \n {lista}")

