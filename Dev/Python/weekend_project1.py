tasks = []
while True:
    print('Menu:\n 1. Add tast \n 2. Show tasks \n 3. Exit')
    try:
        choice = int(input('Choose menu option (1, 2, 3): '))
        if choice == 1:
            task = input('Enter your new task: ')
            tasks.append(task)
            print('New task added in tasks list!')
        elif choice == 2:
            if not tasks:
                print('Task list is empty!')
            else:
                for el in tasks:
                    print(f'Task: {el}')
        elif choice == 3:
            print('Bye bye!')
            break
        else:
            print('Uncorrect menu option!')
    except ValueError:
        print('Please enter menu option (1-3)!')

# 1. I'm writing weekend project right now.
# 2. I'll do new tasks from my AI friend on next week
# 3. I eat bread with nut's pasta every morning 
