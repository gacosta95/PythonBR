#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        #Salário Bruto: (5 * 220)        : R$ 1100,00
        #(-) IR (5%)                     : R$   55,00  
        #(-) INSS ( 10%)                 : R$  110,00
        #FGTS (11%)                      : R$  121,00
        #Total de descontos              : R$  165,00
        #Salário Liquido                 : R$  935,00

vht = float(input('Valor da sua hora: '))
qht = float(input('Quantidade de horas trabalhadas: '))
sb = vht*qht #calcula o salario bruto
inss = 10
fgts = 11
descINSS = (inss*sb)/100
Vfgts = (fgts*sb)/100

#Até 900, isento de IR
if sb <=900:
    ir = 0
    descIR = 0

elif sb >900 and sb <=1500:
    ir = 5
    descIR = (ir*sb)/100

elif sb >1500 and sb <=2500:
    ir = 10
    descIR = (ir*sb)/100

elif sb >2500:
    ir = 20
    descIR = (ir*sb)/100

totalDesc = descINSS+descIR
Sliquido = sb-totalDesc

if descIR==0:
    descIR = 'Isento'


print('Salario Bruto:'.ljust(35),": R$",str(sb).replace('.',','))
print('(-)IR ({}%)'.format(ir) .ljust(35),": R$ {}" .format(descIR))
print('(-)INSS (10%)'.ljust(35),": R$",str(descINSS).replace('.',','))
print('FGTS (11%)'.ljust(35),': R$',str(Vfgts).replace('.',','))
print('Total descontos'.ljust(35),": R$",str(totalDesc).replace('.',','))
print('Salário Liquido'.ljust(35),": R$",str(Sliquido).replace('.',','))
