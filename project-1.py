todo_list = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        for i, task in enumerate(todo_list):
            status = "✅" if task['done'] else "❌"
            print(f"{i + 1}. {task['task']} [{status}]")

def add_task():
    task_name = input("Enter task: ")
    todo_list.append({'task': task_name, 'done': False})
    print("Task added!")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        todo_list[index]['done'] = True
        print("Task marked as done!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        todo_list.pop(index)
        print("Task deleted!")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-5.")
