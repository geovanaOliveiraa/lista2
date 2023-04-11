frase = input("Digite uma frase: ")
espacos = 0

for caractere in frase:
    if caractere == " ":
        espacos += 1

print("A frase digitada contém", espacos, "caracteres em branco.")
