"""
for i in range (5):
    print(f"repetição {i}")
"""

"""numero = int(input("Qual numero voce quer descobrir o fatorial? "))
fatorial = 1

if numero < 0:
    print("NAO EXISTE FATORIAL PARA NUMERO NEGATIVO")
else:
    for i in range (1, numero +1):
        fatorial *= i

    print(f"Fatorial de {numero} é {fatorial}")
    """

""""

base = int(input("Digite o numero Base"))
quantidade = int(input("digite a quantidade de termos "))

valor = base


for i in range (quantidade):
    print(valor, end= " ")
    valor *= base

"""
maior = None
menor = None

for i in range (1, 6):
    numero = float(input(f"Digite o {1 + i}º numero: "))
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero 
    
print(f"Maior numero é: {maior}")
print(f"Menor numero é: {menor}")