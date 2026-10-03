litros = float(input("Quantos litros atualmente tem no carro: "))
consumoCarro = float(input("Quantos KM por Litro o carro faz: "))
distancia = float(input("Qual a distancia até o destino final: "))

kmPossivel = litros * consumoCarro

if distancia <= kmPossivel:
    print("Voce consegue Chegar")
else:
    print("Voce Nao consegue Chegar")