n1 = int(input("numero da operação: "))
n2 = int(input("numero da operação: "))
oper = str(input("Qual operação +,-,*,/"))
resultado = 0
if oper == "+":
    resultado = n1+n2
    print(resultado)
elif oper == "-":
    resultado = n1-n2
    print(resultado)
elif oper == "*":
    resultado = n1*n2
    print(resultado)
elif oper == "-":
    resultado = n1/n2
    print(resultado)
