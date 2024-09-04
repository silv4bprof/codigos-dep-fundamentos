# Recebe um número do usuário
numero = int(input("Digite um número inteiro: "))

positivo = numero > 0
negativo = numero < 0

if positivo:
    print("O número é positivo.")
elif negativo:
    print("O número é negativo.")
else:
    print("O número é zero.")

multiplo_de_3 = numero % 3 == 0

if multiplo_de_3:
    print("O número é múltiplo de 3.")
else:
    print("O número não é múltiplo de 3.")

par = numero % 2 == 0

if par:
    print("O número é par.")
elif not par:  # Corrigido: 'else' é suficiente aqui
    print("O número é ímpar.")

# Causa um erro intencional: divisão por zero
# Erro: Divisão por zero quando o número é zero
resultado = 10 / (numero % 2)

print("Resultado da divisão:", resultado)
