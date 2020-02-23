# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de
# um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""
speed = float(input("Internet: "))
file = float(input("Tamanho do arquivo: "))
calc = (file / speed) / 8
print(round(calc,2),"Minutos")

