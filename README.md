# TP_git_Emie_Suhayl

HELLO
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

def delete_task(task_dict, task_name):
    """
    Delete a task from the task dictionary.
    """
    if task_name in task_dict:
        del task_dict[task_name]
        print(f"Task '{task_name}' deleted successfully.")
    else:
        print(f"Task '{task_name}' not found.")



