qtdAlunos = int(input("Quantos alunos tem: "))
aprovados = 0
for i in range(qtdAlunos):
    mediaFinal = float(input("Media geral do aluno"))
    if mediaFinal >= 7:
        aprovados += 1

porctAlunosAprov = (aprovados / qtdAlunos) * 100
print(f"{porctAlunosAprov} do total da sala foram aprovados")