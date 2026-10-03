from collections import deque
# fila = deque()

# # Adicionar os numeros (10, 5, 15) na pilha:
# fila.append(0)
# fila.append(1)
# fila.append(2)
# fila.append(3)

# # Pegar o ultimo elemento adicionado a pilha:
# elemento = fila.popleft()
# print(elemento) 

# lista = [
#     [   
#         ["ALLAN", "BENTO", "CADU"],
#         ["DAVI", "ESTEVAO", "FELIPE"],
#         ["GABRIEL", "HIGOR", "IGNACIO"]
#     ],
#     [   
#         ["JOAO", "KAIO", "LUCAS"],
#         ["MARIO", "NAVARRO", "OTTO"],
#         ["PAULO", "QUIRINO", "RAFAEL"]
#     ],
#     [   
#         ["SAMUEL", "THIAGO", "ULISSES"],
#         ["VINICIUS", "WILLIAN", "XAVIER"],
#         ["YAGO", "ZECA", "ARTHUR"]
#     ]
# ]


# for predio in lista:
#     for andar in predio:
#         for ap in andar:
#             print(ap)

lista = [
    [   
        ["ALLAN", "BENTO", "CADU"],
        ["DAVI", "ESTEVAO", "FELIPE"],
        ["GABRIEL", "HIGOR", "IGNACIO"]
    ],
    [   
        ["JOAO", "KAIO", "LUCAS"],
        ["MARIO", "NAVARRO", "OTTO"],
        ["PAULO", "QUIRINO", "RAFAEL"]
    ],
    [   
        ["SAMUEL", "THIAGO", "ULISSES"],
        ["VINICIUS", "WILLIAN", "XAVIER"],
        ["YAGO", "ZECA", "ARTHUR"]
    ]
]

nome = input("Quero saber onde mora o: ")
nome.upper


for predio in lista:
    for andar in predio:
        for ap in andar:
            print(ap)
