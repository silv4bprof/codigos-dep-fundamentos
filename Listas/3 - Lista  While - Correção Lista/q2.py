while True:
    numero = int(input("\n-> Digite um número inteiro positivo: "))
    if numero < 0:
        print(f"{numero} é um número negativo, encerrando.")
        break

    contador_digitos = 0
    numero_original = numero

    # Laço while para contar os dígitos com base na divisão inteira por 10, se o número for maior que 0
    # // divisão inteira para desconsiderar a parte flutuante (depois da vírgula)
    while numero > 0:
        print(f"\nDivisão Inteira: {numero} // 10")
        numero = numero // 10
        print(f"Resultado: {numero}")
        contador_digitos += 1
        print(f"Contador: {contador_digitos}")

    # Se o número for 0, o número de dígitos é 1
    if numero_original == 0:
        contador_digitos = 1

    print(f"O número {numero_original} possui {contador_digitos} dígitos.")
