"""senha = input("Digite sua Senha")
confirmaSenha = input("Confirme dua SENHA")

while senha != confirmaSenha:
    print("SENHAS Incorreta")
    confirmaSenha = input("Confirme dua SENHA")
while senha == confirmaSenha:
    print("Acesso Permitido")
    break
    """

preçoProduto = float(input("Qual o preço do produto?"))
total = 0
qtdItens = 0

while preçoProduto != 0:
    total += preçoProduto
    qtdItens += 1
    preçoProduto = float(input("Qual o preço do novo produto?"))

print("O total da compra ", total)
print("A quantidade de itens comprados ", qtdItens)