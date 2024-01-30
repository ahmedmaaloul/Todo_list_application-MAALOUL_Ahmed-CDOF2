#imports
import json

class ToDoList:
    def _init_(self):
        # Initialize an empty task list and then load tasks from the JSON file if available
        self.tasks = []
        self.load_tasks()

    def save_tasks(self):
        # Save the current state of tasks to a JSON file
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        # Load tasks from a JSON file at the start of the application
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or is invalid, start with an empty task list
            self.tasks = []

    def add_task(self, task):
        # Add a new task to the list and save the updated list to the file
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def delete_task(self, task_index):
        # Delete a task based on its index and update the file
        # Check if the provided index is valid
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()
        else:
            print("Invalid task number.")

    def complete_task(self, task_index):
        # Mark a task as completed and save the change
        # Verify the validity of the index
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
        else:
            print("Invalid task number.")

    def display_tasks(self):
        # Display all tasks with their index and completion status
        for idx, task in enumerate(self.tasks):
            status = "Done" if task['completed'] else "Pending"
            print(f"{idx}. {task['task']} [{status}]")

def main():
    # Create an instance of ToDoList and enter the main application loop
    todo_list = ToDoList()

    while True:
        # Display the main menu and handle user input
        print("\nToDo List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # Handle the different choices
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            try:
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice = '3':
            try:
                task_number = int(input("Enter task number to complete: "))
                todo_list.complete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if _name_ == "_main_":
    main()