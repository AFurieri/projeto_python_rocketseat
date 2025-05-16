def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa":nome_tarefa, "completa": False}
    tarefas.append(tarefa)

    print(f"tarefa '{nome_tarefa}' adicionada com sucesso")
    return

def visualizar_tarefas(tarefas):
    print("\nlista de tarefas: ")

    for i, tarefa in enumerate(tarefas, start=1):
        status = "[✓]" if tarefa["completa"] else "[ ]"
        print(f"{i}. {status} {tarefa['tarefa']}")
     
lista_tarefas = [] 

while True:
        print("\nmenu do gerenciamento de tarefas:\n")
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
            adicionar_tarefa(lista_tarefas, tarefa)

        elif escolha == "2": 
            visualizar_tarefas(lista_tarefas)

            
