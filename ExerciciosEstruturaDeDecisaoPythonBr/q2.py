"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

valor = int(input("Digite um valor numérico: "))

if valor == 0:
    print(f"{valor} é zero")
elif valor > 0:
    print(f"{valor} é positivo")
else:
    print(f"{valor} é negativo")
