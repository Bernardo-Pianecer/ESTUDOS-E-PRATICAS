idade = int(input("Qual a idade do cliente: "))
estudante = input("É estudante: ")

if idade >=65 or idade <=12:
    print("Ganha Meia-Entrada")
elif estudante == "sim" or "SIM" or "Sim":
    print("Ganha Meia-Entrada")
else:
        print("Não Ganha Meia-Entrada")

