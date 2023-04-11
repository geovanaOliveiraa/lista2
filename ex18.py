texto = input("Digite um texto: ")
texto_modificado = ""

for caractere in texto:
    codigo_ascii = ord(caractere)
    if codigo_ascii >= 65 and codigo_ascii <= 90:
        codigo_ascii -= 32
    novo_caractere = chr(codigo_ascii)
    texto_modificado += novo_caractere

print("Texto modificado:", texto_modificado)

