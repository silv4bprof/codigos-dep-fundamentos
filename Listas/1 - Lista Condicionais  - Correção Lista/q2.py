nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 70:
    print("Aluno Aprovado!")
elif media >= 50:
    print("Aluno em recuperação!")
    nota_recuperacao = int(input("Nota obtida na recuperação: "))
    nova_media = (media + nota_recuperacao) / 2

    if nova_media >= 70:
        print("Aluno aprovado após a recuperação!")
    else:
        print("Aluno reprovado após a recuperação!")
else:
    print("Aluno Reprovado!")