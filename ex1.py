VG = "aeiou"
num_VG = 0

palavra = input("Digite uma palavra: ")

for letra in palavra:
    if letra in VG:
        num_VG += 1

print("A palavra", palavra, "possui", num_VG, "vogais.")
