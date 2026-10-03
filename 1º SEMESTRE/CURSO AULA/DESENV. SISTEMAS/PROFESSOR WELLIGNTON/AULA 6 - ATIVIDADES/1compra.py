preço = float(input("Qual o preço da compra: "))
pago = float(input("Qunato foi pago: "))

if pago > preço:
    troco = pago - preço
    print(f"O valor do troco é {troco}")
elif pago == preço:
    print("Pagamento sem Troco")
else:
    saldoDevedor = preço - pago
    print(f"Falta pagar {saldoDevedor}")
