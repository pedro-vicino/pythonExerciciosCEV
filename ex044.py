"""elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
-à vista dinheiro/cheque: 10% de desconto
-à vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros"""

preço = float(input("Digite o valor do produto: "))
opcoes = int(input("""Digite a forma de pagamento
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Escolha uma das opções: """))

if opcoes == 1 :
    total = preço - (preço * 10/100)
    print(f"O preço do produto foi de R${preço} para R${total}, utilizando dinheiro/cheque.")
elif opcoes == 2 :
    total = preço - (preço * 5/100)
    print(f"O preço do produto foi de R${preço} para R${total}, utilizando cartão à vista.")
elif opcoes == 3 :
    print(f"Você escolher parcelar em 2x no cartão, assim cobrando R${preço / 2} por mês")
elif opcoes == 4 :
    parcelas = int(input("Quantas parcelas?: "))
    total = preço + (preço * 20/100)
    totalparcelado = total / parcelas
    print(f"""Você escolher parcelar em {parcelas}x no cartão, assim cobrando R${totalparcelado} por mês
O preço, antes de R${preço}, passou a ser R${total}, pois pagamentos de 3x ou mais possuem 20% de juros.""")
else :
    print("Você digitou uma opção inexistente.")