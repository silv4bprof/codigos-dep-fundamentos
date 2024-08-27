renda_anual = float(input("Digite sua renda anual: R$ "))

if renda_anual > 60000:
    taxa = 0.20
elif renda_anual >= 30000:
    taxa = 0.15
else:
    taxa = 0.1

imposto = renda_anual * taxa
renda_final = renda_anual - imposto

print(
    f"""
Renda anual: R$ {renda_anual:.2f}
Taxa aplicada: {taxa * 100}%
Valor do imposto: R$ {imposto:.2f}
Valor final após imposto: R$ {renda_final:.2f}
""")