string = input("Digite uma sequência de 0's e 1's: ")

marcador = 0

for caractere in string:
    if caractere == "1":
       marcador += 1

print("A sequência obtem", marcador, "1's.")
