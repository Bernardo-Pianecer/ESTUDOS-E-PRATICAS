carrinhos = []
precosUnit = []
quants = []
precosProd = []
totalFinal = 0
while True:
    item = input("Produto (ou FIM para encerrar): ")

    if item.upper() == "FIM":
        print("\n====== RECIBO ======")
        for i in range(len(carrinhos)):
            print(f"Produto: {carrinhos[i]}")
            print(f"Preço Unitário: R$ {precosUnit[i]:.2f}")
            print(f"Quantidade: {quants[i]}")
            print(f"Total do Produto: R$ {precosProd[i]:.2f}")
    

            print("----------------------")
            
        break
    
    precoUnit = float(input("Preço Unitário: "))
    quant = int(input("Quantidade: "))

    precoProd = precoUnit * quant
    totalFinal += precoProd

    carrinhos.append(item)
    precosUnit.append(precoUnit)
    quants.append(quant)
    precosProd.append(precoProd)
print(f"Total do Final: R$ {totalFinal:.2f}")