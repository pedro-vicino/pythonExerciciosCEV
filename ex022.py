'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- nome com todas as letras maiúsculas
- nome com todas as letras minúsculas
- quantas letras ao todo (sem considerar espaços)
- quantas letras tem o primeiro nome'''

nomeUsuário = str(input("Digite seu nome: "))
nomeSplit = nomeUsuário.split()
print(nomeUsuário.upper())
print(nomeUsuário.lower())
print("Seu nome possui {} letras!".format(len("".join(nomeSplit))))
print("Seu primeiro nome possui {} letras!".format(len(nomeSplit[0])))
