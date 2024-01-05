"""melhorar o jogo do desafio 028 onde o computador vai 
pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer"""


#a cada palpite o computador muda o número

# import math, random
# palpites = 1
# usuario = int(input("Tente adivinhar o número entre 1 e 10: "))
# num = random.randint(1, 10)
# while num != usuario :
#     usuario = int(input(f"Você errou, o computador escolheu {num}. Tente novamente: "))
#     num = random.randint(1, 10)
#     palpites += 1
# if num == usuario :
#     print(f"Parabéns, você acertou com {palpites} palpites! O computador também escolheu o número {num}")

# a cada palpite o computador avisa se o número digitado pelo usuário precisa ser menor ou maior
import random
palpites = 1
usuario = int(input("Tente adivinhar o número entre 1 e 10: "))
num = random.randint(1, 10)
while num != usuario :
    palpites += 1
    if usuario > num :
        usuario = int(input("Menos... Digite novamente: "))
    elif usuario < num :
        usuario = int(input("Mais... Digite novamente: "))
if num == usuario :
    print(f"Parabéns, você acertou com {palpites} palpites! O computador também escolheu o número {num}")