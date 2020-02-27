# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
med = (n1 + n2) / 2
if med >= 7.0 and med < 10.0:
    print("Média: ", round(med, 2), " Aprovado!")
elif med == 10.0:
    print("Média: ", round(med, 2), " Aprovado com distinção!")
elif med < 7.0:
    print("Média: ", round(med, 2), " Reprovado!! ")
else:
    print("Erro!")
