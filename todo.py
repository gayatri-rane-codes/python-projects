import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"  {i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("\nEnter task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Task '{title}' added.")

def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    print("Welcome to your To-Do List!")

    while True:
        print("\nWhat do you want to do?")
        print("  1. View tasks")
        print("  2. Add task")
        print("  3. Mark task as done")
        print("  4. Delete task")
        print("  5. Quit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")

main()