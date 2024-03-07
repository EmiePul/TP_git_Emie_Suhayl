def add_task(task_dict, task_name, task_description, task_deadline):
    """
    Add a new task to the task dictionary.
    """
    task_dict[task_name] = {
        'description': task_description,
        'deadline': task_deadline,
        'completed': False
    }



def delete_task(task_dict, task_name):
    """
    Delete a task from the task dictionary.
    """
    if task_name in task_dict:
        del task_dict[task_name]
        print(f"Task '{task_name}' deleted successfully.")
    else:
        print(f"Task '{task_name}' not found.")



def mark_task_completed(task_dict, task_name):
    """
    Mark a task as completed in the task dictionary.
    """
    if task_name in task_dict:
        task_dict[task_name]['completed'] = True
        print(f"Task '{task_name}' marked as completed.")
    else:
        print(f"Task '{task_name}' not found.")
