# Inicialização de Variáveis
# a lista tbm pode ser aberta como nome = []
lista_de_tarefas = list()
continuar = True

def exibir_menu():
    """Exibe o menu de escolha"""
    print("Escolha uma opção: \n " \
    "1 - Inseir nova tarefa \n " \
    "2 - Listar Tarefas \n " \
    "3 - Deletar Tarefa \n" \
    "4 - Sair ")


def adicionar_tarefa(lista_de_tarefas, tarefa):
    """Adiciona uma tarefa a uma lista pré-existente"""
    lista_de_tarefas.append(tarefa)
    print("tarefa adicionada com sucesso")
    return lista_de_tarefas

def listar_tarefa(lista_de_tarefas):
    """Exibe a lista de tarefas criada"""
    print ("-" * 50)
    print(f"{" " * 15} Lista de Tarefas")
    print ("-" * 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f"{n} {tarefa}")
        n += 1 # Isso é igual a escrever n = n + 1

def deletar_tarefa(lista_de_tarefas, tarefa):
    """Deleta uma única tarefa da lista pré-existente a partir do número"""
    lista_de_tarefas.pop((tarefa - 1))
    return lista_de_tarefas

while continuar:
    # Loop principal
    
    exibir_menu()

    opcao = input("insira o que deseja fazer: ")

    print("\n")
    
    if opcao == "1":
        tarefa = input("Insira uma nova tarefa: ")
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefa(lista_de_tarefas)
    elif opcao == "3":
        # A validação verifica se valor é número e depois se ele está presente na lista
        tarefa = input("insira o número da tarefa que deseja deletar: ")
        if not tarefa.isnumeric():
             print("Númeor inválido! Tente novamente")
        elif int(tarefa) > len(lista_de_tarefas):
            print("Númeor inválido! Tente novamente")
        elif tarefa <= 0: 
             print("Númeor inválido! Tente novamente")
        else:
            deletar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "4":
        continuar = False
    else: 
        print("Opção inválida! Por favor tente novamente.")
    print("\n")


    

    