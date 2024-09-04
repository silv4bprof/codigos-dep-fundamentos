# total = 0
# while True:
#     numero = int(input("Digite um número: "))
#     if numero != 0:
#         total = total + numero
#     else:
#         break
# print(f"Total: {total}")

total = 0
numero = int(input("Digite um número: "))
while numero != 0:
    total = total + numero
    numero = int(input("Digite um número: "))
print(f"Total: {total}")
