import json

# Open and reads the JSON file to get the task list, generates an empty list if the file is not found
def load_tasks(filepath="tasks.json"):
    try:
        with open(filepath, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Export tasks to a JSON file
def save_tasks(tasks, filepath="tasks.json"):
    with open(filepath, 'w') as file:
        json.dump(tasks, file, indent=4)

# Insert a new task description
def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append({"description": task, "completed": False})
    print(f"Task '{task}' added.")

# Display all current tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['description']} [{status}]")

# Set a task's status to completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            # Get the task description before marking it as completed
            task_description = tasks[task_num - 1]["description"]
            tasks[task_num - 1]["completed"] = True
            print(f"Task '{task_description}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task by its number
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task '{deleted_task['description']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function for the To-Do List App
def todo_list_app():
    print("Welcome to my To-Do List App :)")

    tasks = load_tasks()

    while True:
        print("\nWhat would you like to do?:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            confirm_exit = input("Are you sure you want to exit? (Yes(Y)/No(N)): ").upper()
            if confirm_exit == "Y":
                save_tasks(tasks)
                print("Saving tasks...\nTasks saved. Thank you for using my To-Do List App :) Goodbye!")
                break
            else:
                print("Returning to the main menu...")
        else:
            print("Invalid choice. Please choose a number (1-5)")

# Main function to start script execution
if __name__ == "__main__":
    todo_list_app()
