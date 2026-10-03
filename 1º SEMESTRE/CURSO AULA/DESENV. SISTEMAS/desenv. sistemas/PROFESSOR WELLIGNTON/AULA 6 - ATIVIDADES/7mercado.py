total = 0

while True:
    nome_produto = input("Digite o nome do produto (ou 'FIM' para encerrar): ")

    if nome_produto.upper() == "FIM":
        break

    preco_unitario = float(input("Digite o preço unitário: "))
    quantidade = int(input("Digite a quantidade: "))

    preco_produto = preco_unitario * quantidade

    total += preco_produto


print(f"Total da compra: R${total:.2f}")