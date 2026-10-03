alunos = int(input("Quantos alunos: "))
aprovados = 0

for i in range(alunos):

    nota1 = float(input(f"Nota1 aluno {i+1}:"))
    nota2 = float(input(f"Nota2 aluno {i+1}:"))
    nota3 = float(input(f"Nota3 aluno {i+1}:"))

    media = ((nota1+nota2+nota3)/3)

    if media >= 7:
        aprovados += 1

print("Quantidade de Aprovados ",aprovados)