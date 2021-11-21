"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  #Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0        A
  #Entre 7.5 e 9.0         B
  #Entre 6.0 e 7.5         C
  #Entre 4.0 e 6.0         D
  #Entre 4.0 e zero        E
  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""
import os

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
os.system("clear")

med = (nota1+nota2)/2

if med >=9.0 and med <=10.0:
    conceito = 'A'

elif med >=7.5 and med <9.0:
    conceito = 'B'

elif med >=6.0 and med <7.5:
    conceito = 'C'

elif med >=4.0 and med <6.0:
    conceito = 'D'

elif med <4.0:
    conceito ='E'


print("Sua primeira nota é: ",nota1)
print("Sua segunda nota é: ",nota2)
print("Sua média é: ",med)
print("Conceito: ",conceito)
if med >=6.0 and med <=10.0:
    print("APROVADO!")
elif med <6.0:
    print('REPROVADO!')



