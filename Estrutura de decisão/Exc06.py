# Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input("Numero 01: "))
n2 = int(input("Numero 02: "))
n3 = int(input("Numero 03: "))
lista = [n1, n2, n3]
maior = max(lista) #max, uma função nativa do python capaz de pegar o maior valor de uma lista

print("Maior: ",maior)