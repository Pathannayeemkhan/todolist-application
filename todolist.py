import json
import os
from datetime import datetime

# Define the file to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file if it exists, else initialize an empty list
tasks = []
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r") as file:
        tasks = json.load(file)

def save_tasks():
    # Save tasks to the file
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task(task, priority, due_date):
    # Add a new task to the list
    tasks.append({"task": task, "priority": priority, "due_date": due_date, "completed": False})
    save_tasks()

def remove_task(task_index):
    # Remove a task from the list by index
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks()

def mark_completed(task_index):
    # Mark a task as completed by index
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks()

def list_tasks():
    # Display tasks in a list with details
    for index, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} (Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status})")

# Main program loop
while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. List Tasks")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task description: ")
        priority = input("Enter task priority (high, medium, low): ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        add_task(task, priority, due_date)

    elif choice == "2":
        list_tasks()
        task_index = int(input("Enter task index to remove: "))
        remove_task(task_index)

    elif choice == "3":
        list_tasks()
        task_index = int(input("Enter task index to mark as completed: "))
        mark_completed(task_index)

    elif choice == "4":
        list_tasks()

    elif choice == "5":
        print("Exiting Task Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

