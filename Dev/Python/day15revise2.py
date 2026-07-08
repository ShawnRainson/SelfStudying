tasks = ["  buy some milk ", "", "Short task", "This is a very long task that should definitely be ignored by your code because it is too long"]

def clear_and_filter_tasks(raw_tasks):
    clear_tasks = []
    for line in raw_tasks:
        line = str(line)
        line = line.strip()
        line = line.replace('buy', 'purchase')
        if line != "" and len(line) <= 50:
            clear_tasks.append(line)
                    

    print(clear_tasks)

clear_and_filter_tasks(tasks)
            