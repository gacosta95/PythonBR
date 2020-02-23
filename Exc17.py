""""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores
para cima, isto é, considere latas cheias.
"""
import math as mt
lataG = 18
galao = 3.6
repita = 0
lCobertura = lataG * 6
valorLata = 80.00
valorGalao = 25.00
gCobertura = galao * 6


metrosQuadrado = float(input("Tamanho da área (Metros quadrados) "))
demaos = int(input("Quantas demãos você deseja aplicar? "))
qtdNec_Lata = (metrosQuadrado * demaos) / lCobertura #Calcula a quantidade necessária de tinta para pintar a área
qtdNec_Galao= (metrosQuadrado * demaos) / gCobertura#Calcula aquantidade necessária de tintar para pintar a área com base nos galões
valorG = qtdNec_Galao * valorGalao #calcula o valor do Galão
valorL = qtdNec_Lata* valorLata #Calcula o valor da lata de 18 litros
litrosLataP = (qtdNec_Lata * 18)
litrosNG = int(litrosLataP / 18)
litrosFaltam = (litrosLataP / 18 - litrosNG) * 18
latas_n = litrosFaltam / galao
print("\nGalões de tintas: ".ljust(10), mt.ceil(qtdNec_Galao), "".ljust(6), "Valor: R$", round(valorG, 2))
print("Latas de tintas: ".ljust(18), mt.ceil(qtdNec_Lata), "".ljust(6), "Valor: R$", round(valorL, 2))

if(latas_n <= 3):
    latas_n = mt.ceil(latas_n)
else:
    latas_n = 0
    litrosNG = litrosNG + 1
    print("Compre: ", litrosNG, "lata(s) 18L\nE", latas_n)

"""
math.ceil() para arredondar o valor para cima
ljust() para definir um espaçamento para a direita
rjust() para definir um espaçamento para esquerda
"""
