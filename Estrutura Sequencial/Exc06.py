#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
pi = 3.14 #Como 3,14 é o valor mais próximo do pi, eu o atribui há variavel pi

r = float(input("Digite o raio do circulo: "))
e = r**2 #Eleva  o raio ao quadrado
result = pi * e #multiplica o pi pelo raio elevado ao quadrado

print("A área do circulo é = ",result)# Resultado