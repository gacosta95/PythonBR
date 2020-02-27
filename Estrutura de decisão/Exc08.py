# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.
prod1 = float(input("Valor produto 1: "))
prod2 = float(input("Valor produto 2: "))
prod3 = float(input("Valor produto 3: "))
lista = [prod1, prod2, prod3]
barato = min(lista)
if prod1 == barato:
    print("Produto 1: ", barato, "R$")
elif prod2 == barato:
    print("Produto 2: ",barato,"R$")
elif prod3 == barato:
    print("Produto 3: ", barato, "R$")
else:
    print("Erro!!")