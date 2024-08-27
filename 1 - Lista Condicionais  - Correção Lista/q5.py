pergunta_1 = int(input("Pergunta 1 [1 - sim | 0 - não]: "))
pergunta_2 = int(input("Pergunta 2 [1 - sim | 0 - não]: "))
pergunta_3 = int(input("Pergunta 3 [1 - sim | 0 - não]: "))
pergunta_4 = int(input("Pergunta 4 [1 - sim | 0 - não]: "))
pergunta_5 = int(input("Pergunta 5 [1 - sim | 0 - não]: "))

num_positiva = pergunta_1 + pergunta_2 + pergunta_3 + pergunta_4 + pergunta_5

if num_positiva == 5:
    print("Assassino!")
elif num_positiva >= 3:
    print("Cúmplice")
elif num_positiva == 2:
    print("Suspeito")
else:
    print("inocente")