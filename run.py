to_do_list = []
def add_task(task):
    """
    Add a new task to the to-do list.
    The task is stored as a dictionary with 'task' and 'done' status.
    """
    to_do_list.append({'task': task, 'done': False})
    print(f'Task {task} added successfully!\n')

