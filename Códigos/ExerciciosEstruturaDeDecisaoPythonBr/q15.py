"""
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""

ladoA = int(input("Lado A: "))
ladoB = int(input("Lado B: "))
ladoC = int(input("Lado C: "))

if (ladoA + ladoB) > ladoC and (ladoC + ladoA) > ladoB and (ladoB + ladoC) > ladoA:
    print("É um triângulo", end=" ")

    if ladoA == ladoB and ladoB == ladoC and ladoC == ladoA:
        print("equilátero")
    elif ladoA == ladoB or ladoB == ladoC or ladoC == ladoA:
        print("isósceles")
    elif ladoA != ladoB and ladoB != ladoC and ladoC != ladoA:
        print("escaleno")
else:
    print("Não é um triângulo")
