# TP_git_Emie_Suhayl

HELLO
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


def add_task(task_dict, task_name, task_description, task_deadline):
    """
    Add a new task to the task dictionary.
    """
    task_dict[task_name] = {
        'description': task_description,
        'deadline': task_deadline,
        'completed': False
    }

