print("usando while true:")
while True:
    pergunta = input("A gente já chegou? ")
    if pergunta == "sim":
        break
print("Chegou!")

print("\nUsando while <condição>")
chegou = input("A gente já chegou? ")
while chegou == "nao":
    chegou = input("A gente já chegou? ")
print("Chegou")
