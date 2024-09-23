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

