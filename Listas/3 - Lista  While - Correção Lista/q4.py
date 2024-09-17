# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa o multiplicador
multiplicador = 0

# Laço while para exibir a tabuada
while multiplicador <= 10:
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
    # Incrementa o multiplicador
    multiplicador += 1
