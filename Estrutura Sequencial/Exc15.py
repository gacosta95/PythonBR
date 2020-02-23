"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para
o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

total_Horas = float(input("Digite o total de horas trabalhadas: "))
valor_Horas =float (input("Digite o valor por horas trabalhada: "))
salario = total_Horas * valor_Horas
percent_ir = (11*salario)/100
percent_inss = (8*salario)/100
percent_sindc = (5*salario)/100
liquido = salario - percent_ir - percent_inss - percent_sindc

print("Salario Bruto = ",salario,"R$")
print("Imposto de renda = ",percent_ir,"R$")
print("INSS = ",percent_inss,"R$")
print("Sindicato  = ",percent_sindc,"R$")
print("Salario liquido = ", liquido,"R$")