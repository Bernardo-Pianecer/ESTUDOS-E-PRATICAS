n1 = float(input("Digite o primeiro numero da operação"))
n2 = float(input("Digite o segundo numero da operação"))
resultado = 0
operação = str(input("Digite uma operação das a seguir (+, -, * ou /): "))


match operação:
    case  "+":
        resultado = n1 + n2
        print(resultado)
    case  "-":
        resultado = n1 - n2
        print(resultado)
    case  "*":
        resultado = n1 * n2
        print(resultado)
    case  "/":
        resultado = n1 / n2
        print(resultado)