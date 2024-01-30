class ToDoList:
    def __init__(self):
        # Initializes an empty list to store tasks
        self.tasks = []

    def add_task(self, task):
        # Adds a new task to the list. Each task is a dictionary with 'task' and 'completed' keys
        self.tasks.append({'task': task, 'completed': False})

    def delete_task(self, task_index):
        # Deletes a task based on its index. Checks for valid index to prevent errors
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task number.")

    def complete_task(self, task_index):
        # Marks a task as completed. Verifies index validity before updating
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
        else:
            print("Invalid task number.")

    def display_tasks(self):
        # Displays all tasks with their indices and completion status
        for idx, task in enumerate(self.tasks):
            status = "Done" if task['completed'] else "Pending"
            print(f"{idx}. {task['task']} [{status}]")

def main():
    todo_list = ToDoList()

    while True:
        # Main application loop displaying the menu and handling user input
        print("\nToDo List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '3':
            task_number = int(input("Enter task number to complete: "))
            todo_list.complete_task(task_number)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
