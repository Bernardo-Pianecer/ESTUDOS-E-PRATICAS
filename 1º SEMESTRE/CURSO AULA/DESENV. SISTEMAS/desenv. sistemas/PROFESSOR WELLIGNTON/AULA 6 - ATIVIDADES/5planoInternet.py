consmMensalGB = int(input("Qual o seu gasto mensal em GB:"))

if consmMensalGB <= 50:
    print("Plano Básico (R$ 39,90)")
elif consmMensalGB <= 150:
    print("Plano Intermediário (R$ 69,90)")
else:
    print("Plano Premium (R$ 119,90)")