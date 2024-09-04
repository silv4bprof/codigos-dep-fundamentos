"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    - Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
    - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

import math

# Entrada dos coeficientes
a = float(input("Digite o valor de a: "))

if a != 0:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    # Cálculo de delta
    delta = b**2 - 4 * a * c

    if delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)  # remover math.sqrt()
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)  # remover math.sqrt()
        print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A equação possui uma raiz real: {raiz:.2f}")
    else:
        print("A equação não possui raízes reais, pois delta é negativo")
else:
    print("O valor de a não pode ser 0")
