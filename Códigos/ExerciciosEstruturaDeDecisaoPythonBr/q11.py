"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
 - salários até R$ 280,00 (incluindo) : aumento de 20%
 - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
 - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
 - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
 - o salário antes do reajuste;
 - o percentual de aumento aplicado;
 - o valor do aumento;
 - o novo salário, após o aumento.
"""

salario_base = float(input("Digite seu salário: "))

if salario_base <= 280:
    novo_salario = salario_base + (salario_base * 0.2)
    percentual_aumento = 0.2
elif salario_base > 208 and salario_base < 700:
    novo_salario = salario_base + (salario_base * 0.15)
    percentual_aumento = 0.15
elif salario_base > 700 and salario_base < 1500:
    novo_salario = salario_base + (salario_base * 0.1)
    percentual_aumento = 0.1
elif salario_base >= 1500:
    novo_salario = salario_base + (salario_base * 0.05)
    percentual_aumento = 0.05

percentual_aumento = percentual_aumento * 100

print(f"Salário base: R$ {salario_base:.2f}")
print(f"Percentual de aumento: {percentual_aumento}%")
print(f"Valor do aumento: R$ {(novo_salario - salario_base):.2f}")
print(f"Salário ajustado: {novo_salario:.2f}")
