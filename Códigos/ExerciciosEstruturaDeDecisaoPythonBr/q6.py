"""Faça um Programa que leia três números e mostre o maior deles."""

numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))
numero3 = int(input("Terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} é o maior")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} é o maior")
else:  # elif numero3 > numero1 and numero3 > numero2:
    print(f"{numero3} é o maior")
