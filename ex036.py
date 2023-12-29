"""escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado"""
valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário: "))
anos = int(input("Em quantos anos será pago?: "))
anosEmMeses = anos * 12
prestacao = valor / anosEmMeses
salario30 = (salario * 30/100)
if prestacao > salario30 :
    print(f"Empréstimo negado. A prestação mensal é de R${prestacao}, e excedeu 30% do seu salário, que é R${salario30}.")
else :
    print(f"Empréstimo aceito!")