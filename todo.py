import json
from datetime import datetime

# Task class
class Task:
    def __init__(self, description, priority, due_date, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

# Function to add a task
def add_task(tasks):
    description = input("Enter task description: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append(Task(description, priority, due_date))

# Function to remove a task
def remove_task(tasks):
    list_tasks(tasks)
    task_index = int(input("Enter task number to remove: "))
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def mark_task_completed(tasks):
    list_tasks(tasks)
    task_index = int(input("Enter task number to mark as completed: "))
    if 0 <= task_index < len(tasks):
        tasks[task_index].completed = True
    else:
        print("Invalid task number.")

# Function to list all tasks
def list_tasks(tasks):
    for idx, task in enumerate(tasks):
        status = "Completed" if task.completed else "Pending"
        print(f"{idx}: {task.description} [Priority: {task.priority}, Due: {task.due_date}, Status: {status}]")

# Function to save tasks to a file
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

# Function to load tasks from a file
def load_tasks(filename='tasks.json'):
    tasks = []
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            for task_data in tasks_data:
                tasks.append(Task(**task_data))
    except FileNotFoundError:
        pass
    return tasks

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Mark Task as Completed\n4. List Tasks\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '2':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
            save_tasks(tasks)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
