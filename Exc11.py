"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1 - o produto do dobro do primeiro com metade do segundo .
2 - a soma do triplo do primeiro com o terceiro.
3 - o terceiro elevado ao cubo.
"""
in1 = int(input("Digite o primeiro numero inteiro: "))
in2 = int(input("Digite o segundo numero interiro: "))
real =  (input("Digite um numero real: "))

d = in1*2
m = in2/2
p = d + m
print("O produto do dobro do primeiro com a metade do segundo é = ",p)
t = in1*3 + p
print("A soma do triplo do primeiro com o terceiro é = ", t)
cubo = 3*t
print("O terceiro elevado ao cubo é = ", cubo)