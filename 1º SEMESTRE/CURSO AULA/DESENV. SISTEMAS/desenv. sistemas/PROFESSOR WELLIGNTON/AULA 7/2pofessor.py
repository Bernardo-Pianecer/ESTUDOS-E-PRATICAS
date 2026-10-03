antesNotas = [7.5 , 8.0 , 6.2 , 9.1, 5,5]
depoisNotas = [7.5 , 8.0 , 6.2 , 9.1, 5,5]
print(antesNotas)
qtdNotas = int(input("Quantas notas corrigir?"))
for i in range(qtdNotas):
    numNota = int(input("Qual nota voce quer trocar?"))
    nota = float(input("Qual a nova nota"))
    depoisNotas[numNota - 1] = nota
print(f"Antes: {antesNotas}")
print(f"Depois: {depoisNotas}")