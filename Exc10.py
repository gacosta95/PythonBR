#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
print("Conversor simples de graus Celsius para graus farenheit")
c = float(input("Graus celsius: "))
f = round (c*1.8 + 32,2)
print(f," Graus Farenheit")