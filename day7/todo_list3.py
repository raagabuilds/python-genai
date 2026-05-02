import os

def show_menu():
    print("1. Add task\n2. View tasks\n3. Remove task\n4. Quit")
    
def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return [line.strip() for line in f]

def save_tasks(filename, tasks):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(tasks):
    new_task = input("Enter task: ")
    tasks.append(new_task)
    save_tasks("tasks.txt", tasks)
    print(f"Added: {new_task}")

def show_tasks(tasks):
    if len(tasks)==0:
        print("No Tasks")
    else:
        print("Your tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def remove_task(tasks):
    if len(tasks) == 0:
            print("No tasks to remove.")
            return
    show_tasks(tasks)
    num = int(input("Which task to remove? "))
    removed = tasks.pop(num - 1)
    save_tasks("tasks.txt", tasks) 
    print(f"Removed: {removed}")

tasks=load_tasks("tasks.txt")

while True:
    show_menu()
    choice=int(input("Pick your choice: "))
    if choice == 1:
        add_task(tasks)
    elif choice == 2:
        show_tasks(tasks)
    elif choice == 3:
        remove_task(tasks)
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")