qtdAlunos = int(input("Quantos Alunos: "))
nomeAprovados = []
nomeRecuperaçao = []
nomeReprovados = []


for i in range(1,qtdAlunos):
    nome = input("Qual o nome do aluno: ")
    notaFinal = float(input("Qual a sua nota final"))
    if notaFinal >= 7:
        nomeAprovados.append(nome)
    elif notaFinal >=5:
        nomeRecuperaçao.append(nome)
    else:
        nomeReprovados.append(nome)
print(f"Os alunos aprovados são: {nomeAprovados}")
print(f"Os alunos de recuperação são: {nomeRecuperaçao}")
print(f"Os alunos reprovados são: {nomeReprovados}")

