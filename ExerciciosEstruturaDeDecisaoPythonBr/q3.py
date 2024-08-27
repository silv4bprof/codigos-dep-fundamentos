"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

letra = input("Digite F ou M: ")

if letra == "m" or letra == "M":
    print("M - Masculino")
elif letra == "f" or letra == "F":
    print("F - Feminino")
else:
    print("Sexo inválido")
