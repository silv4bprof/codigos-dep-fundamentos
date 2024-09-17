"""
Tipos de divisão:

/ -> Divisão normal: Realiza a divisão entre operandos
// -> Divisão inteira: Realiza a divisão entre operandos e a parte decimal do resultado
% -> Módulo: Retorna o resto da divisão entre operandos
"""

n1 = 250
n2 = 3

print(f"Exemplos com {n1} dividido por {n2}:")
print(f"\nDivisão Normal ({n1} / {n2})")
print("Obs.: Resto quebrado se houver")
print(n1 / n2)

print(f"\nDivisão Inteira ({n1} // {n2})")
print("Obs.: Ignora o resto após a virgula")
print(n1 // n2)

print(f"\nMódulo/Resto da Divisão (({n1} % {n2})")
print("Obs.: O que sobra depois de todas as iterações")
print(n1 % n2)
