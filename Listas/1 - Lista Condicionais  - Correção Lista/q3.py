ano = int(input("Digite o ano: "))

print("Alternativa 01")

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} NÃO é bissexto!")

print("Alternativa 02")

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"{ano} é bissexto!")
        else:
            print(f"{ano} NÃO é bissexto!")
    else:
        print(f"{ano} é bissexto!")
else:
    print(f"{ano} NÃO é bissexto!")