nome = input("insira um nome:")
sexo = input("insira o sexo (m/f):")
idade = input("insira a idade:)

if sexo.upper() == "F" and idade < 25:
    print(nome, "aceita")
else:
    print("Não aceita")
