# Usando while True
while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    if login != senha:
        break
    print("Tente novamente!")
print("Acesso aceito!")

# Usando while <condição>
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

while login == senha:
    print("Login e senha não podem ser iguais.\nTente novamente!")
    senha = input("Digite sua senha novamente: ")
print("Tudo certo, nada errado!")
