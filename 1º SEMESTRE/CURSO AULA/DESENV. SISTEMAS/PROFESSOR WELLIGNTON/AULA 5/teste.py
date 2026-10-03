compra = float(input("Digite o Valor da compra"))
valorFinal = 0

if compra > 500:
    print("Seu desconto é de 15%")
    valorFinal = compra * 0,15
    print(f"Sua compra deu [valorFinal]")
elif compra >=200:
    print("Seu desconto é de 10%")
    valorFinal = compra * 0,10
    print(f"Sua compra deu [valorFinal]")
elif compra:
    print("Seu desconto é de 0%")
    valorFinal = compra
    print(f"Sua compra deu [valorFinal]")