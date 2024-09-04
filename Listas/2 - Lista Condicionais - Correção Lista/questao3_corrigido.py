# Recebe um número do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é positivo ou negativo
positivo = numero > 0
negativo = numero < 0

if positivo:
    print("O número é positivo.")
elif negativo:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Verifica se o número é múltiplo de 3
multiplo_de_3 = (numero % 3 == 0)

if multiplo_de_3:
    print("O número é múltiplo de 3.")
else:
    print("O número não é múltiplo de 3.")

# Verifica se o número é par ou ímpar
par = (numero % 2 == 0)

if par:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Corrigido: evita divisão por zero
if numero % 2 != 0:  # Apenas faz a divisão se o número não for zero
    resultado = 10 / (numero % 2)
    print("Resultado da divisão:", resultado)
else:
    print("Não é possível realizar a divisão por zero.")
