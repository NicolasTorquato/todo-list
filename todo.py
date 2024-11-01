import json
from datetime import datetime

class Task:
    def __init__(self, title, due_date, priority, completed=False):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def __str__(self):
        return f"Task(title='{self.title}', due_date='{self.due_date}', priority='{self.priority}', completed={self.completed})"


class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            return []  # Retorna uma lista vazia se o arquivo não existir
        except json.JSONDecodeError:
            print("Erro: O arquivo tasks.json está vazio ou mal formado.")
            return []  # Retorna uma lista vazia se houver erro de decodificação

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def display_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa encontrada.")
            return
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")  # Exibe o índice junto com a tarefa

    def add_task(self, title, due_date, priority):
        task = Task(title, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
        else:
            print("Índice da tarefa inválido.")
    
    def edit_task(self, index):
        if 0 <= index < len(self.tasks):
            print("Edição da Tarefa:")
            title = input("Novo Título da tarefa: ")
            due_date = input("Novo Prazo da tarefa (YYYY-MM-DD): ")
            priority = input("Nova Prioridade (alta, média, baixa): ")
            self.tasks[index].title = title
            self.tasks[index].due_date = due_date
            self.tasks[index].priority = priority
            self.save_tasks()
        else:
            print("Índice da tarefa inválido.")          

    def list_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def list_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
        else:
            print("Índice da tarefa inválido.")

    def filter_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar Tarefa")
            print("2. Marcar Tarefa como Concluída")
            print("3. Listar Tarefas Pendentes")
            print("4. Listar Tarefas Concluídas")
            print("5. Remover Tarefa")
            print("6. Filtrar Tarefas por Prioridade")
            print("7. Sair")

            choice = input("Escolha uma opção (1-7): ")

            if choice == '1':
                title = input("Título da tarefa: ")
                due_date = input("Prazo da tarefa (YYYY-MM-DD): ")
                priority = input("Prioridade (alta, média, baixa): ")
                self.add_task(title, due_date, priority)
            elif choice == '2':
                self.display_tasks()
                index = int(input("Índice da tarefa a ser concluída: "))
                self.complete_task(index)
            elif choice == '3':
                print("\nTarefas Pendentes:")
                for task in self.list_pending_tasks():
                    print(task)
            elif choice == '4':
                print("\nTarefas Concluídas:")
                for task in self.list_completed_tasks():
                    print(task)
            elif choice == '5':
                self.display_tasks()
                index = int(input("Índice da tarefa a ser removida: "))
                self.remove_task(index)
            elif choice == '6':
                priority = input("Digite a prioridade para filtrar (alta, média, baixa): ")
                print("\nTarefas com prioridade '{}':".format(priority))
                for task in self.filter_tasks_by_priority(priority):
                    print(task)
            elif choice == '7':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")


# Exemplo de uso
if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.menu()