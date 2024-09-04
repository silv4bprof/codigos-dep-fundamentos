"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
"""

ano = int(input("Digite o ano: "))

# se divisível por 4, é bissexto
if ano % 4 == 0:
    # se divisível por 100 -> verificar se é divisível por 400
    # se não for divisível por 100 mas for divisível por 4, é bissexto
    if ano % 100 == 0:
        # se chegar a ser divisível por 400, sendo divisível por 100, é bissexto
        if ano % 400 == 0:
            print("É bissexto")
        else:
            print("NÃO é bissexto")
    else:
        print("É bissexto")
else:
    print("NÃO é bissexto")
