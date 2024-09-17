while True:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero == 0:
        print("Encerrando o programa.")
        break

    # Inicializa a variável para verificar a primalidade
    primo = True

    # Verifica se o número é menor ou igual a 1
    if numero <= 1:
        primo = False
    else:
        divisor = 2
        # O motivo de usar numero // 2 é que um divisor de um número não pode ser maior que sua metade (exceto se for o próprio número).
        while divisor <= numero // 2:
            if numero % divisor == 0:
                # Se entrar aqui, quer dizer que o número tem ao menos um divisor além de 1 e dele mesmo.
                primo = False
                break
            divisor += 1
            print(f"Divisor: {divisor}")

    # Exibe o resultado
    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
