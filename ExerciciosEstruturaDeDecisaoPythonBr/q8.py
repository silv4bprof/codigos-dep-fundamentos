"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

preco1 = float(input("Preço do primeiro produto: R$ "))
preco2 = float(input("Preço do segundo produto: R$ "))
preco3 = float(input("preço do terceiro produto: R$ "))


if preco1 < preco2 and preco1 < preco3:
    print("Produto 1 é o mais barato")
elif preco2 < preco1 and preco2 < preco3:
    print("Produto 2 é o mais barato")
elif preco3 < preco1 and preco3 < preco2:
    print("Produto 3 é o mais barato")
