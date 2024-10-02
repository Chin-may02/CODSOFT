tasks = {}

def add_tasks():
    title = input("Enter task title: ")
    content = input("Enter task content: ")
    tasks[title] = content
    print("Task added successfully!")

def view_tasks():
    if tasks:
        print("Your task:")
        for title, content in tasks.items():
            print(f"Title: {title}")
            print(f"Content: {content}")
            print("-" * 20)
    else:
        print("No tasks found.")

def delete_task():
    title = input("Enter title of task to delete: ")
    if title in tasks:
        del tasks[title]
        print(f"Task '{title}' deleted successfully!")
    else:
        print(f"Task '{title}' not found.")

def main_menu():
    while True:
        print("\nTASKER")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Thank you for using the TASKER Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main_menu()
