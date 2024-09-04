conta = 0
valor = float(input("Informe o valor do produto: R$ "))

while valor != 0:
    conta = conta + valor
    valor = float(input("Informe o valor do produto: R$ "))

if conta > 200:
    # conta = conta * 0.95
    # ou
    conta = conta - (conta * 0.05)
print("Total a pagar: R$ ", conta)
