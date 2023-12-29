"""a confederação nacional de natação precisa de um programa que leia 
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-até 9 anos: mirim
-até 14 anos: infantil
-até 19 anos: junior
-até 25 anos: senior
-acima: master"""

import datetime

anoatual = datetime.date.today().year
nascimento = int(input("Qual o seu ano de nascimento?: "))
idade = anoatual - nascimento

if idade < 9 :
    print(f"Você tem {idade} anos e sua categoria é MIRIM")
elif 9 <= idade < 14 :
    print(f"Você tem {idade} anos e sua categoria é INFANTIL")
elif 14 <= idade < 19 :
    print(f"Você tem {idade} anos e sua categoria é JUNIOR")
elif 19 <= idade < 25 :
    print(f"Você tem {idade} anos e sua categoria é SÊNIOR")
else :
    print(f"Você tem {idade} anos e sua categoria é MASTER")