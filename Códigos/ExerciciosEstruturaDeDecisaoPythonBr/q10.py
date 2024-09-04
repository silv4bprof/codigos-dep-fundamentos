"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

turno = input("Turno em que estuda [M - Matutino | V - Vespertino | N - Noturno]: ")

if turno == "m" or turno == "M":
    print("Bom dia!")
elif turno == "v" or turno == "V":
    print("Boa tarde!")
elif turno == "n" or turno == "N":
    print("Boa noite!")
elif turno == "":
    print("Valor inválido")
else:
    print("Valor inválido")
