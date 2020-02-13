#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
print("Conversor simples de Farenheit para Celsius")

F = float(input("Graus Farenheit: "))
C = round (5 * (F-32) / 1.8,2)

print (C," Graus Celsius")
