# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vogais = ["a", "e", "i", "o", "u", "y", "w"]
letra = str(input("Letra: "))

if letra in vogais:
    print("Vogal!")

else:
    print("Consoante!")