#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
letra = str(input("Letra: "))
if letra == "F":
    print(letra," - Feminino!")
elif letra == "M":
    print(letra, " - Masculino!")

else:
    print("Invalido!!!")
