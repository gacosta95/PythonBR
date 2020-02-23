"""""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
de latas de tinta a serem compradas
e o preço total.
"""
custo = 80.00
r = 18 * 3 #Levando em consideração que cada litro cobre 3 metros
d = int(input("Quantas demãos você ira aplicar? ")) #para saber com precisão é necessário considerar o numero de demãos
a = float(input("Metragem ao quadrado de área a ser pintada: "))
c = (a *d) / r
custoFinal = custo * c
print("Cliente precisa comprar ","%.2f" % round(c,2)," Latas de tinta")
print("Valor: ","%.2f" % round(custoFinal,2), "reais")

#Fonte de pesquisa para aprendizado do calculo:df
#https://www.vivendodecoracao.com.br/quantidade-de-ti ta-para-cada-ambiente/
