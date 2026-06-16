"""
Escreva um programa que leia o salário fixo de um
vendedor de uma loja e o total de vendas por ele efetuadas no mês. Acrescente ao salário um
prêmio, conforme a seguinte tabela:

O programa deve calcular e informar o salário final do vendedor e qual foi o prêmio recebido.
"""

S = float(input("informe o salário do vendedor: "))
TV = int(input("informe o total de vendas: "))

premio = 0

if 100 < TV <= 500:
    premio = 50
elif 500 < TV <= 750:
    premio = 70
elif TV > 750:
    premio = 100
else:
    print("informe um valor válido")

print("O salário final do vendedor é", S + premio, "e  o prêmio recebido foi ", premio),"reais"
