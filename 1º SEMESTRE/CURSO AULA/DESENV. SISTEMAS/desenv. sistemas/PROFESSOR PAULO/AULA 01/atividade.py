pilha = []

palavra = "estrutura"

for letra in palavra:
    pilha.append(letra)

invertida = ""

while len(pilha) > 0:
    invertida += pilha.pop()

print(invertida)