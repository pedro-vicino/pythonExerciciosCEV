""" Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente
ex: ana maria de souza
primeiro = ana
ultimo = souza"""

nomeCompleto = str(input("Digite seu nome completo: "))
nomeSplit = nomeCompleto.split()

print('Seu primeiro nome é {}'.format(nomeSplit[0]))
print('Seu último nome é {}'.format(nomeSplit[len(nomeSplit)-1]))


# nomeSplit[len(nomeSplit)-1] : o len(nomeSplit), com o nome Pedro Henrique Vicino,
# por exemplo, tem o resultado 3. Com o -1, ele consegue imprimir o útimo elemento (3 - 1),
# pois o len mostra a quantidade exata de elementos
# que o array possui, sem começar do 0, e sim do 1