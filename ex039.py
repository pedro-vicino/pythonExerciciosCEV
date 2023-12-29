"""Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

import datetime

nascimento = int(input("Qual seu ano de nascimento?: "))
anoatual = datetime.date.today().year
idade = anoatual - nascimento
temporestante = 18 - idade

if idade < 18 :
    print(f"""Você ainda não está pronto para o alistamento.
Você possui {idade} anos e ainda falta {temporestante} ano(s) para se alistar!
O ano do seu alistamento será em {nascimento + 18}""")
elif idade == 18 :
    print(f"""Você deve se alistar agora. 
Com {idade} anos você precisa se alistar!""")
else :
    print(f"""Já passou o tempo para se alistar!
Você deveria ter se alistado há {idade - 18} ano(s).
Seu alistamento foi em {nascimento + 18}.""")
