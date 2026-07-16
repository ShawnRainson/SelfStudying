tasks = []
with open('tasks.txt', 'r', encoding='utf-8') as file:
    for el in file:
        clean_el = el.strip()
        if clean_el:
            tasks.append(clean_el)

def show_menu():
    print('Menu:\n 1. Add task\n 2. Show tasks list\n 3. Exit')
    add_option()

def add_option():
    while True:
        try:
            choice = int(input('Choose option (1-3): '))
            if choice == 1:
                add_task()
            elif choice == 2:
                show_list()
            elif choice == 3:
                print('Bye-bye!')
                save_tasks()
                break
            else:
                print('Invalid option!')
        except ValueError:
            print('Invalid value!')

def add_task():
    new_task = input('Enter new task: ')
    tasks.append(new_task)

def show_list():
    if not tasks:
        print('List is empty!')
    else:
        for task_el in tasks:
            print(f'Task: {task_el}')

def save_tasks():
    with open('tasks.txt', 'w', encoding='utf-8') as file:
        for save_task in tasks:
            if save_task != '':
                file.write(f'{save_task}\n')
         

show_menu()