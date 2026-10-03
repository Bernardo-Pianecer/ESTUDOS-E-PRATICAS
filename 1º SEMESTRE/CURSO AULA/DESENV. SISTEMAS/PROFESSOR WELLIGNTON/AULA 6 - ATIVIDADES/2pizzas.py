pessoas = float(input("Quantas pessoas vai ter na festa: "))
totalFatias = pessoas * 3
QtdPizza = totalFatias // 8
sobra = totalFatias % 8

if sobra > 0:
    QtdFinalPizza = QtdPizza + 1
    print(f"O total de pizza a ser pedido é: {QtdFinalPizza}")
else:
    print(f"O total de pizza a ser pedido é: {QtdPizza}")