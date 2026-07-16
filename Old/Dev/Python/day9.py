tasks = []
def show_menu():
    print('Menu:\n 1. Add task\n 2. Show list\n 3. Exit')
    choose_option()

def choose_option():
    try:
        choice = int(input('Choose menu option (1-3): '))
        if choice == 1:
            add_task()
        elif choice == 2:
            show_list()
        elif choice == 3:
            print('Bye-bye!')
        else:
            print('Invalid option!')
            show_menu()
    except ValueError:
        print('Invalid value!')
        show_menu()

def add_task():
    new_task = input("Enter new task: ")
    tasks.append(new_task)
    show_menu()

def show_list():
    for el in tasks:
        print(f'Task: {el}')
    show_menu()

show_menu()
