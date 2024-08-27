"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

numero1 = int(input('Primeiro numero: '))
numero2 = int(input('Segundo numero: '))
numero3 = int(input('Terceiro numero: '))

maior = numero1
meio = numero2
menor = numero3

# verificando o maior
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

# verificando o menor
if numero1 < menor:
    menor = numero1
if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3

# verificar o do meio
if numero1 != maior and numero1 != menor:
    meio = numero1
elif numero2 != maior and numero2 != menor:
    meio = numero2
else:
    meio = numero3

print(f"Numeros ordenados decrescente: {maior} -> {meio} -> {menor}")