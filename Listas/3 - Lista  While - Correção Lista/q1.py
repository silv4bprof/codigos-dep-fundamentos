soma = 0
contador = 0

numero = int(
    input("Digite um número inteiro positivo (ou um número negativo para parar): ")
)

# Laço while para somar números e contar a quantidade
while numero >= 0:
    soma += numero
    contador += 1
    numero = int(
        input("Digite um número inteiro positivo (ou um número negativo para parar): ")
    )

if contador > 0:
    media = soma / contador
    print(f"A média dos números positivos inseridos é: {media}")
else:
    print("Nenhum número positivo foi inserido.")
