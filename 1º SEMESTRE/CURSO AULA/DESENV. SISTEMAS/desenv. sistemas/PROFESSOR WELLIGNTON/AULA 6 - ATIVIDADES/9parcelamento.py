parcelamento = int(input("O valor do parcelmento: "))

for i in range(1, 13):
    parcela = parcelamento / i
    print(f"{i}x de R$ {parcela/i:.2f}")