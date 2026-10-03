tarefa = []

while True:
    print("\n====== MENU ======")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Mostrar tarefas")
    print("4 - Mostrar quantidade de tarefas")
    print("5 - Sair")

    decisao = int(input("O que voce quer fazer? "))

    # ADICIONAR
    if decisao == 1:
        qntdTarefas = int(input("Quantas tarefas deseja adicionar? "))

        for i in range(qntdTarefas):
            nomeAtv = input(f"Nome da tarefa {i+1}: ")
            tarefa.append(nomeAtv)

        print("Tarefa adicionada com sucesso!")

    # REMOVER
    elif decisao == 2:

        if len(tarefa) == 0:
            print("Nao ha tarefas para remover.")

        else:
            print("\nTAREFAS:")
            for i in range(len(tarefa)):
                print(f"{i} - {tarefa[i]}")

            remover = int(input("Digite o numero da tarefa que deseja remover: "))

            if remover >= 0 and remover < len(tarefa):
                tarefa.pop(remover)
                print("Tarefa removida!")
            else:
                print("Numero invalido.")

    # MOSTRAR TAREFAS
    elif decisao == 3:

        if len(tarefa) == 0:
            print("Nenhuma tarefa cadastrada.")

        else:
            print("\n===== TAREFAS =====")
            for i in range(len(tarefa)):
                print(f"{i+1} - {tarefa[i]}")

    # QUANTIDADE DE TAREFAS
    elif decisao == 4:
        print(f"Quantidade de tarefas: {len(tarefa)}")

    # SAIR
    elif decisao == 5:
        print("Programa encerrado.")
        break

    # OPÇÃO INVALIDA
    else:
        print("Opcao invalida.")