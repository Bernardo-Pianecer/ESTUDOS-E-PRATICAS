idade = int(input("Qual a dua idade: "))

if idade >= 18:
    print("PODE TIRAR A CNH")
else:
    anos = 18 - idade
    print(f"NAO PODE TIRAR A CNH, Faltam {anos} anos")
