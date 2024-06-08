import os

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def delete_task(self, task_index):
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task index!")
        else:
            del self.tasks[task_index]
            print("Task deleted successfully!")

    def update_task(self, task_index, new_task):
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task index!")
        else:
            self.tasks[task_index] = new_task
            print("Task updated successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

def main():
    todo_list = TodoList()
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter index of task to delete: "))
            todo_list.delete_task(index - 1)
        elif choice == '3':
            index = int(input("Enter index of task to update: "))
            new_task = input("Enter new task: ")
            todo_list.update_task(index - 1, new_task)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Thank you for using the To-Do List Application!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
