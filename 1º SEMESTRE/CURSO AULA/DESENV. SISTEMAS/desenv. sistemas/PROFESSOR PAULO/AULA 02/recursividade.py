# def verificar(vetor):
#     if vetor[0] == 8:
#         print("tem 8")
#     else:
#         print("nao tem 8")
#         verificar( vetor[1:])

# verificar([2,4,6,8,10])



# def contagem(n):
#     if n == 0:
#         print("Fim!")
#     else:
#         print(n)
#         contagem(n - 1)
# contagem(10)



# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# qtd = int(input("QUANTAS VEZES: "))
# for i in range(qtd):
#     print(fibonacci(i))

# print(0)
# print(1)
# def contagem(bolso1, bolso2, nu):
#     if nu == 8:
#         print("fim")
#     else:
#         soma1 = (bolso1 + bolso2)
#         print(soma1)
#         contagem(bolso2, soma1, nu+1)
# contagem(0,1,0)


# def inverter(l = ""):
#     if len(l) > 0:
#         print(l[-1])
#         inverter(l[:-1])

# inverter("python")

# vetor = [4,8,1,9,3]

# def maior(vetor, indice=0):
#     if indice == len(vetor) - 1:
#         return vetor[indice]
#     maior_restante = maior(vetor, indice + 1)
#     if vetor[indice] > maior_restante:
#         return vetor[indice]
#     else:
#         return maior_restante

# print(maior(vetor))


