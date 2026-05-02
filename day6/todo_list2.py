def show_menu():
    print("1. Add task\n2. View tasks\n3. Remove task\n4. Quit")
    

def show_tasks():
     if len(tasks)==0:
            print("No Tasks")
     else:
        print("Your task:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def remove_task():
    if len(tasks) == 0:
            print("No tasks to remove.")
            return
    show_tasks(tasks)
    num = int(input("enter the number of which task to be removed? "))
    removed = tasks.pop(num - 1)
    print(f"Removed: {removed}")

def add_task():
    if choice==1:
        print(f"choice: {choice}")
        new_task=(input("Enter task: "))
        tasks.append(new_task)
        print(f"Added: {new_task}")


tasks=[]


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

