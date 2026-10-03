import random
import time

pessoas = [
    {"nome": "andrieli", "peso": 2},
    {"nome": "arthur", "peso": 5},
    {"nome": "bernardo", "peso": 5},
    {"nome": "bryam", "peso": 7},
    {"nome": "bruno", "peso": 5},
    {"nome": "douglas", "peso": 5},
    {"nome": "eduardo d", "peso": 4},
    {"nome": "eduardo p", "peso": 8},
    {"nome": "gabriel a", "peso":5},
    {"nome": "guilherme autista", "peso": 9},
    {"nome": "guilherme m", "peso": 5},
    {"nome": "gustavo", "peso": 6},
    {"nome": "joao", "peso": 5},
    {"nome": "kevin", "peso": 4},
    {"nome": "lesly", "peso": 7},
    {"nome": "isabela", "peso": 0.85},
    {"nome": "matheus", "peso": 6},
    {"nome": "murilo", "peso": 5},
    {"nome": "nicolas", "peso": 9},
    {"nome": "pablo", "peso": 7},
    {"nome": "pedro", "peso": 5},
    {"nome": "rafaela", "peso": 5},
    {"nome": "vinicius", "peso": 6},
    {"nome": "emerson", "peso": 5},
    {"nome": "henrinque anacleto", "peso": 5}
]

while len(pessoas) > 1:
    nomes = [p["nome"] for p in pessoas]
    pesos = [p["peso"] for p in pessoas]

    sorteado = random.choices(nomes, weights=pesos, k=1)[0]

    # encontrar e remover
    for i, p in enumerate(pessoas):
        if p["nome"] == sorteado:
            pessoas.pop(i)
            break

    print(f"Saiu: {sorteado} | Restam: {len(pessoas)} pessoas")
    time.sleep(0.5)

print("Último restante (vencedor):", pessoas[0]["nome"])