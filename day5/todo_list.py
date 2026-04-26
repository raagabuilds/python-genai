tasks=[]
while True:
    print("1. Add task\n2. View tasks\n3. Remove task\n4. Quit")

    choice=int(input("Pick your choice: "))

    if choice==1:
        print(f"choice: {choice}")
        new_task=(input("Enter task: "))
        tasks.append(new_task)
        print(f"Added: {new_task}")

    elif choice==2:
        print(f"Choice:{choice}")
        if len(tasks)==0:
            print("No Tasks")
        else:
            print("Your task:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice==3:
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            num = int(input("enter the number of which task to be removed? "))
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed}")

    elif choice==4:
        print(f"choice:{choice}")
        print("Good bye!")
        break

    else:
        print("Invalid choice")


