"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                     : R$   55,00
    (-) INSS ( 10%)                 : R$  110,00
    FGTS (11%)                      : R$  121,00
    Total de descontos              : R$  165,00
    Salário Liquido                 : R$  935,00
"""

valor_hora = float(input("Valor/hora: "))
horas_trabalhadas = int(input("Horas trabalhadas: "))

salario_base = valor_hora * horas_trabalhadas
total_desconto = 0

# desconto IR (tem como melhorar - diminuir código)
if salario_base <= 900:
    desconto_ir = 0
elif salario_base <= 1500:
    desconto_ir = salario_base * 0.05
elif salario_base <= 2500:
    desconto_ir = salario_base * 0.1
elif salario_base > 2500:
    desconto_ir = salario_base * 0.2

salario_descontado_ir = salario_base - desconto_ir

# desconto INSS
desconto_inss = salario_base * 0.1
salario_descontado_inss = salario_base - desconto_inss

# desconto FGTS
salario_descontado_fgts = salario_base - (salario_base * 0.11)
total_desconto = desconto_ir + desconto_inss

print(f"Salário Bruto             : R$ {salario_base:.2f}")

if salario_base <= 900:
    print(f"(-) IR (5%)             : Isento")
elif salario_base <= 1500:
    print(f"(-) IR (5%)               : R$ {salario_base - salario_descontado_ir:.2f}")
elif salario_base <= 2500:
    print(f"(-) IR (11%)             : R$ {salario_base - salario_descontado_ir:.2f}")
elif salario_base > 2500:
    print(f"(-) IR (20%)             : R$ {salario_base - salario_descontado_ir:.2f}")

print(f"(-) INSS ( 10%)           : R$ {salario_base - salario_descontado_inss:.2f}")
print(f"FGTS (11%)                : R$ {salario_base - salario_descontado_fgts:.2f}")
print(f"Total de descontos        : R$ {total_desconto:.2f}")
print(f"Salário Liquido           : R$ {(salario_base - total_desconto):.2f}")

# CORRIGIR
