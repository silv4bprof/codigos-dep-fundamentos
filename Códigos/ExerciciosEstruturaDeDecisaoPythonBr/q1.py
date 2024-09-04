"""Faça um Programa que peça dois números e imprima o maior deles."""

numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))

if numero1 > numero2:
    print(f"Maior número entre {numero1} e {numero2}: {numero1}")
else:
    print(f"Maior número entre {numero1} e {numero2}: {numero2}")
