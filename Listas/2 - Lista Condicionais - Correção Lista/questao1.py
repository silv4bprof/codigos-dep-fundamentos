# Entrada de dados
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
valor_hora = float(input("Digite o valor da hora normal: "))

# Constantes
adicional_extra = valor_hora * 0.50  # Adicional de 50% do valor da hora normal
hora_extra = valor_hora + adicional_extra  # Valor da hora extra
horas_extras = 0

# Cálculo do salário
if horas_trabalhadas > 160:
    horas_normais = 160
    horas_extras = horas_trabalhadas - 160
    salario = (horas_normais * valor_hora) + (horas_extras * hora_extra)
else:
    salario = horas_trabalhadas * valor_hora

# Exibição do resultado
print("\nResultado:")
print(f"Horas trabalhadas: {horas_trabalhadas:.2f} h")
print(f"Horas extras trabalhadas: {horas_extras:.2f} h")
print(f"Valor hora extra: R$: {hora_extra:.2f}")
print(f"Valor das horas extras: R$ {(horas_extras * adicional_extra):.2f}")
print(f"Salário total do mês: R$ {salario:.2f}")
