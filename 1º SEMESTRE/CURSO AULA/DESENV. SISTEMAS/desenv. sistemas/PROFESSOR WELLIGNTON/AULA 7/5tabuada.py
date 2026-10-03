num = float(input("Voce quer Saber a tabuada de que numero: "))
maxNum = int(input("Voce quer até que numero: "))

for i in range(0,maxNum):
    print(f"{num} x {i+1} = {num * (i+1)}")