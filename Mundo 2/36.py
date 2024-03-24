"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

casa = int(input("Digite o valor da casa: "))
salario = int(input("Digite o seu salário: "))
anos = int(input("Quantos anos deseja pagar: ")) * 12

presta = casa / anos
condicao = salario * 0.3
if(presta > condicao):
    print("Emprestimo Negado.")
else:
    print("Emprestimo Aprovado.")