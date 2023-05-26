tasks = {}

def counter_tasks(list):
    return len(list) + 1

def add_task():
    item = input("...")
    counter = counter_tasks(tasks)
    tasks[counter] = {'item': item, 'status': 'incompleto'}

def tasks_completed():
    show_tasks(tasks)
    indice = int(input('Qual tarefa você deseja marcar como completa? '))
    if indice in tasks:
        tasks[indice]['status'] = "completo"

def tasks_incomplete():
    show_tasks(tasks)
    indice = int(input('Qual tarefa você deseja marcar como incompleta? '))
    if indice in tasks:
        tasks[indice]['status'] = "incompleto"

def remove_item():
    show_tasks(tasks)
    delete = int(input("Qual item você deseja excluir? "))
    for item in list(tasks):
        if item == delete:
            tasks.pop(item)

def show_tasks(list):
    if len(list) == 0:
        print('A lista esta vazia!')
    else:
        for item, val in list.items():
            print('-----------------------')
            print(f"{item} - desc: {val['item']} - status: {val['status']}")

def control():
    print("\n----- Checklist -----\n")
    print("Escolha uma opção:")
    print("1. Adicionar tarefa")
    print("2. Exibir tarefas")
    print("3. Marcar como completa")
    print("4. Marcar como incompleta")
    print("5. Remover tarefa")
    print("6. Sair")

    option = input("Opção selecionada: ")

    if option == "1":
        add_task()
    elif option == '2':
        show_tasks(tasks)
    elif option == "3":
        tasks_completed()
    elif option == '4':
        tasks_incomplete()
    elif option == "5":
        remove_item()
    elif option == '6':
        print("Encerrando o programa...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")




while True:
    control()

