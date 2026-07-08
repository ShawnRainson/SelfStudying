tasks_list = ['Learn english (Pending)', 'Complete first week (Complete)', 'Learn python (Pending)', 'Finish second week (Complete)', 'Create repository (Complete)']
def get_task_stats(task_list):
    count_tasks = {}
    comp_tasks = 0
    pend_tasks = 0
    for state in task_list:
        if "Complete" in state:
            comp_tasks += 1
        elif "Pending" in state:
            pend_tasks += 1
    count_tasks["completed"] = comp_tasks
    count_tasks["pending"] = pend_tasks
    return count_tasks

counted_tasks = get_task_stats(tasks_list)
print(counted_tasks)
