listPar = []
maxList = int(input("Até que numero voce quer descobrir os pares: "))

for i in range(1, maxList):
    if i % 2 == 0:
        print(f"{i} é par")