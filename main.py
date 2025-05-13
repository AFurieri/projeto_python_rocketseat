def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa":nome_tarefa, "completa": False}
    tarefas.append(tarefa)

    print(f"tarefa '{nome_tarefa}' adicionada com sucesso")
    return

tasks = []

while True:
        print("\nmenu do gerenciamento de listas\n")
        print("opção 1: adicionar tarefa")
        print("opção 2: visualizar tarefas")
        print("opção 3: atualizar tarefa")
        print("opção 4: completar tarefa")
        print("opção 5: deletar tarefas completadas")
        print("opção 6: sair") 

        escolha = input("digite a opção que você deseja acionar ")

        if escolha == "6":
            break

        elif escolha == "1":
            tarefa = input("digite a tarefa que você deseja adicionar ")
            adicionar_tarefa(tasks, tarefa)

print(tasks)
            
