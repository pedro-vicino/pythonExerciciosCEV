# Faça um programa que leia algo pelo 
# teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela

verificar = input("Digite qualquer valor, sendo número ou palavra: ")
print("O valor é um número?", verificar.isnumeric())
print("O valor é uma palavra?", verificar.isalpha())
print("O valor é uma palavra toda em letra maiúsculo?", verificar.isupper())
print("O valor é um palavra toda em letra minúscula?", verificar.islower())
print("O valor é uma palavra e um número ao mesmo tempo?", verificar.isalnum())
print("O valor é apenas um espaço?", verificar.isspace())