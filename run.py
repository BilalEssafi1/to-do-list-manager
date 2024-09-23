to_do_list = []


def add_task(task):
    """
    Add a new task to the to-do list.
    The task is stored as a dictionary with 'task' and 'done' status.
    """
    to_do_list.append({'task': task, 'done': False})
    print(f'Task {task} added successfully!\n')


def show_tasks():
    """
    Displays the list of tasks with their current status.
    If no tasks are available, it notifies the user.
    """
    if not to_do_list:
        print("Your to-do list is emtpy!/n")
    else:
        print("Your to do list:")
        for idx, task in enumerate(to_do_list):
            status = "Done" if task['done'] else "Pending"
            print(f"{idx +1}. {task['task']} - {status}")
        print()


def remove_task(index):
    """
    Removes a task from the to-do list by its index.
    Check if the index is valid before attempting removal.
    """
    try:
        task = to_do_list.pop(index)
        print(f'Task "{task["task"]}" removed successfully!\n')
    except IndexError:
        print("Invalid task number. Please try again!\n")


def mark_task_done(index):
    """
    Mark a task as done by its index.
    Check if the index is valid before marking it as complete
    """
    try:
        to_do_list[index]['done'] = True
        print(f'Task "{to_do_list[index]["task"]} marked as completed!\n')
    except IndexError:
        print("Invalid task number. Please try again!\n")


def display_menu():
    """
    Displays the menu options to the user.
    """
    print("To-Do List Manager:")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. Mark a task as done")
    print("4. Show all tasks")
    print("5. Exit\n")


def main():
    """
    Main function that runs the To-Do List Manager.
    It continously prompts the user for input and calls the
    appropriate functions.
    """
    while True:
        display_menu()
        choice = input("Choose an option(1-5): \n")

        if choice == "1":
            task = input("Enter the task description: \n")
            add_task(task)

        elif choice == "2":
            show_tasks()
            try:
                task_num = int(input("Enter the task number to remove:\n"))-1
                remove_task(task_num)
            except ValueError:
                print("Please enter a valid number.\n")

        elif choice == "3":
            show_tasks()
            try:
                task_num = int(input("Enter task number to mark as done:\n"))-1
                mark_task_done(task_num)
            except ValueError:
                print("Please enter a valid number.\n")

        elif choice == "4":
            show_tasks()

        elif choice == "5":
            print("Exiting the to-do list\n")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 5.\n")


main()