"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

Divisões:

/ = Divisão normal: retorna um número ponto flutuante, mesmo que a divisão seja exata.
Exemplo: 7 / 3 = 2.333...5

// = Divisão inteira: Retorna a parte inteira da divisão, descartando a parte decimal.
Exemplo: 7 // 3 = 2.333...5 -> (2)

% = Módulo da divisão (resto): retorna o resto da divisão entre dois números
Exemplo: 7 % 3 = 1 (resto)
"""

numero = int(input("Número [< 1000]: "))

if numero < 1000:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    print(f"{numero} contém", end=" ")

    if centenas > 0:
        print(f"{centenas} centena(s)", end=" ")
    if dezenas > 0:
        print(f"{dezenas} dezena(s)", end=" ")
    if unidades > 0:
        print(f"e {unidades} unidade(s).")
else:
    print("Número deve ser menor que 1000.")
