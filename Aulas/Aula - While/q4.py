# fibonacci

termos = int(input("Quantidade de termos da sequência: "))

# n1 é quem vai ser atualizado a cada iteração do while
n1 = 0
n2 = 1
contador = 0

print(n1, end=" ")
while contador < termos:
    n3 = n1 + n2
    # atualizando n1 e n2
    n1 = n2
    n2 = n3

    # atualizando contador
    contador += 1

    # exibindo valor atualizado
    print(n1, end=" ")
