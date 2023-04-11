vetA = list("computação")
VETb = []

palavra = input("Digite uma palavra de 10 letras: ")

for i in range(len(VETa)):
    if palavra[i].lower() == VETa[i].lower():
        VETb.append(palavra[i])
    else:
        VETb.append("_")

print("vetA:", "".join(VETa))
print("vetB:", "".join(VETb))
