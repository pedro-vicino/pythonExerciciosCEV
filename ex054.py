"""crie um programa que leia o ano de nascimento de sete pessoa. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""

import datetime
anoatual = datetime.date.today().year
pessoa = 1
maior = 0
menor = 0
for ano in range(1, 8) :
    nascimento = int(input(f"Em que ano a {pessoa}ª pessoa nasceu?: "))
    pessoa += 1
    idade = anoatual - nascimento
    if idade >= 18 :
        maior += 1
    else :
        menor += 1
print(f"Dos nacimentos citados, {maior} são maiores de idade e {menor} são menores de idade")