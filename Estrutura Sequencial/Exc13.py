"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
 utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
sexo = int(input("Sexo:  1 = Homem | 2 = Mulher: "))
if sexo == 1:
    h = float(input("Qual é a sua altura? "))
    c = 72.7*h
    r = c - 58
    print("Seu peso ideal é = ",r)

elif sexo == 2:
    h = float(input("Qual é a sua altura? "))
    c = 62.1 * h
    r = c - 44.7
    print("Seu peso ideal é = ", r)
else:
    print("Invalido! Cientificamente falando existem apenas dois sexos! Não complica...")