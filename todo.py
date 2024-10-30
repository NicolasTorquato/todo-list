import json
from datetime import datetime

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()

    def complete_task(self, index):
        self.tasks[index].completed = True
        self.save_tasks()

    def list_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def list_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def remove_task(self, index):
        del self.tasks[index]
        self.save_tasks()

    def filter_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            return []

# Exemplo de uso
if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.add_task("Estudar Python", "2023-10-30", "alta")
    todo_list.add_task("Fazer compras", "2023-10-25", "média")
    print(todo_list.list_pending_tasks())