tasks = {}

def add_task():
    title = input("Enter task title: ")
    content = input("Enter task content: ")
    tasks[title] = content
    print("Task added ")

def view_tasks():
    if tasks:
        print("Your tasks:")
        for title, content in tasks.items():
            print(f"Title: {title}")
            print(f"Content: {content}")
            print("-" * 20)
    else:
        print("No tasks found.")

def update_task():
    title = input("Enter title of task to update: ")
    if title in tasks:
        new = input("Have you completed the task : ")
        tasks[title] = new
        print(f"Task '{title}' updated")
    else:
        print(f"Task '{title}' not found.")

def main_menu():
    while True:
        print("\nTASKER")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. Update a Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            print("Thank you")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 4.")

if __name__ == "__main__":
    main_menu()
