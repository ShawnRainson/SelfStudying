tasks = ['Learn english', 'Learn python', 'Learn csharp', 'create repository']
def find_task_by_title(task_list, search_title):
    search_title = search_title.lower()
    titles = []
    for title in task_list:
        title = title.lower()
        titles.append(title)
    if search_title in titles:
        return f'Founded task: {search_title}'
    else:
        return None

find_task = find_task_by_title(tasks, 'LEARN ENGLISH')
print(find_task)
find_task = find_task_by_title(tasks, 'Learn UNITY')
print(find_task)