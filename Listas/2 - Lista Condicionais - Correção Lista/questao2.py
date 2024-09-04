# Definindo os preços por litro
preco_alcool = 1.90
preco_gasolina = 2.50

# Entrada de dados
tipo_combustivel = int(
    input("Digite o tipo de combustível (1 - alcool & 2 - gasolina): ")
)
litros = float(input("Digite a quantidade de litros: "))

# Inicializando variáveis
valor_total = 0
preco_litro = 0
desconto_percentual = 0
nome_combustivel = ""

# Calculando o valor total e desconto com base no tipo de combustível
if tipo_combustivel == 1:
    preco_litro = preco_alcool
    nome_combustivel = "álcool"
    valor_total = litros * preco_litro

    # Aplicando desconto para álcool
    if litros <= 20:
        desconto_percentual = 3
    else:
        desconto_percentual = 5

elif tipo_combustivel == 2:
    preco_litro = preco_gasolina
    nome_combustivel = "gasolina"
    valor_total = litros * preco_litro

    # Aplicando desconto para gasolina
    if litros <= 20:
        desconto_percentual = 6  # Desconto fixo de 6% para gasolina
    else:
        desconto_percentual = 8

else:
    print("Tipo de combustível inválido.")
    exit()

# Calculando o valor do desconto
valor_desconto = valor_total * desconto_percentual / 100

# Calculando o valor total a pagar após o desconto
valor_a_pagar = valor_total - valor_desconto

# Exibindo os resultados
print(f"Preço do litro de {nome_combustivel}: R$ {preco_litro:.2f}")
print(f"Desconto aplicado: {desconto_percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total sem desconto: R$ {valor_total:.2f}")
print(f"Valor total a pagar: R$ {valor_a_pagar:.2f}")
