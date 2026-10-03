nomes = []
qtdNomes = int(input("Quantos nomes na LISTA: "))

for i in range(qtdNomes):
    numNome = input(f"Qual o {i+1}° nome: ")
    nomes.append(numNome)

print("Lista Original: ", nomes)
nomes.reverse()
print(f"Lista Invertida: ", nomes)