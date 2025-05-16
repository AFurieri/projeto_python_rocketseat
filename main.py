def adicionar_tarefa(tarefas, nome_tarefa):
    """adiciona uma tarefa solicitada a lista de tarefas"""
    tarefa = {"tarefa":nome_tarefa, "completa": False}
    tarefas.append(tarefa)

    print(f"tarefa '{nome_tarefa}' adicionada com sucesso")
    return

def visualizar_tarefas(tarefas):
    """visualiza a lista com todas as tarefas e mostra se estão concluidas ([✓]) ou não ([ ])"""
    print("\nlista de tarefas: ")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "[✓]" if tarefa["completa"] else "[ ]"
        print(f"{i}. {status} {tarefa['tarefa']}")
    return

def atualizar_nome_tarefas (tarefas, numero_tarefa, nova_tarefa):
    """recebe o numero da tarefa, que deseja ser alterada, na lista de tarefas e troca o nome dela"""
    tarefas[numero_tarefa - 1] = {"tarefa":nova_tarefa, "completa": False}
    print(f"tarefa{numero_tarefa} atualizada para {nova_tarefa}")
    return
     
lista_tarefas = [] 

while True:
        print("\nmenu do gerenciamento de tarefas:\n")
        print("opção 1: adicionar tarefa")
        print("opção 2: visualizar tarefas")
        print("opção 3: atualizar nome da tarefa")
        print("opção 4: completar tarefa")
        print("opção 5: deletar tarefas completadas")
        print("opção 6: sair") 

        escolha = input("\ndigite a opção que você deseja acionar\n")

        if escolha == "6":
            break

        elif escolha == "1":
            tarefa = input("digite a tarefa que você deseja adicionar ")
            adicionar_tarefa(lista_tarefas, tarefa)

        elif escolha == "2": 
            visualizar_tarefas(lista_tarefas)

        elif escolha == "3":
            visualizar_tarefas(lista_tarefas)
            tarefa_para_atualizar = int(input("digite o numero da tarefa que você deseja atualizar "))
            nova_tarefa = input("digite o nome da nova tarefa ")
            atualizar_nome_tarefas(lista_tarefas, tarefa_para_atualizar, nova_tarefa)



            
