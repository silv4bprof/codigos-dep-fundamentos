angulo1 = int(input("Angulo 1: "))
angulo2 = int(input("Angulo 2: "))
angulo3 = int(input("Angulo 3: "))

soma_angulos = angulo1 + angulo2 + angulo3

if soma_angulos == 180:
    print("É um triângulo!")
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("Retângulo")
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print("Obtuso")
    else:
        print("Acuto")
else:
    print("Não é um triângulo")
